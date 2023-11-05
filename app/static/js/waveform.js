
const canvas = document.getElementById("output");
canvas.width = 400;
canvas.height = 400;
const ctx = canvas.getContext("2d");
const AudioContext = window.AudioContext || window.webkitAudioContext;
let raf
let audioContext
if (raf) {
  cancelAnimationFrame(raf)
}

const numberOfSides = 512
const size = 100
const x = canvas.width / 2
const y = canvas.height / 2
const lineWidth = 10
const lineColor = '#5a8fef'
const audioAmplifier = 100


/*
 * Draw the Circle Waveform based on the audio buffer from meyda
 */
function draw(buffer) {

  if (buffer === undefined || buffer === null) {
    ctx.arc(x, y, size, 0, 2 * Math.PI);
    ctx.strokeStyle = lineColor
    ctx.lineWidth = lineWidth
    ctx.stroke()

    return
  }

  ctx.beginPath();

  // Create audio-reactive polygons
  for (var i = 0; i < numberOfSides; i++) {

    const audioValue = buffer[i] * audioAmplifier
    const cos = Math.cos(i * 2 * Math.PI / numberOfSides)
    const sin = Math.sin(i * 2 * Math.PI / numberOfSides)
    const x1 = x + size * cos - audioValue // * (i % 2 === 1 ? -1: 1)
    const y1 = y + size * sin + (i % 2 === 1 ? audioValue : 0)

    if (i === 0) {
      ctx.moveTo(x1, y1);
    } else {
      ctx.lineTo(x1, y1);
    }
  }

  ctx.closePath()
  ctx.strokeStyle = lineColor
  ctx.lineWidth = lineWidth
  ctx.stroke()
}




/**
 * - Get the mic input
 * - Setup audioContext to use with Meyda
 * - Create a rAF loop that calls draw()
 */
(async function() {
  let stream = null

  try {
    stream = await navigator.mediaDevices.getUserMedia({
      audio: {
        echoCancellation: false
      }
    });
  } catch (err) {
    throw new Error(err)
  }

  if (audioContext) audioContext.close();
  audioContext = new AudioContext({
    latencyHint: "interactive"
  });

  const source = audioContext.createMediaStreamSource(stream);

  const meyda = new Meyda.createMeydaAnalyzer({
    audioContext,
    source,
    bufferSize: numberOfSides,
    windowingFunction: "rect"
  });

  loop = delta => {
    raf = requestAnimationFrame(loop)

    ctx.fillRect(0, 0, canvas.width, canvas.height);
    const buffer = meyda.get('buffer')
    draw(buffer)
  };

  raf = requestAnimationFrame(loop)
})();