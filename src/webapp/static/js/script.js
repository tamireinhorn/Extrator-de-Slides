let myVideo;

window.URL = window.URL || window.webkitURL;
// Get the video file input field
const videoInput = document.getElementById('video-file');
videoInput.onchange = setFileInfo;

function setFileInfo() {
  let files = this.files;
  myVideo = files[0];
  let video = document.createElement('video');
  video.preload = 'metadata';

  video.onloadedmetadata = function() {
    window.URL.revokeObjectURL(video.src);
    let duration = video.duration;
    myVideo.duration = duration;
    updateInfos();
  }

  video.src = URL.createObjectURL(files[0]);;
}

let slideNumber = document.getElementById('slide-number');
slideNumber.addEventListener('input', (event) => {
  const slideDuration = myVideo.duration / slideNumber.value;
  document.getElementById('slide-duration-info').textContent = `This means that we'll try to get a slide every ${slideDuration.toFixed(2)} seconds.`
});


function updateInfos() {
  let infos = document.getElementById('video-duration-info');
  let slideControl = document.getElementById('slide-control');
  slideControl.style.display = 'block';
  infos.textContent = `Your video has a duration of ${myVideo.duration} seconds.`;
  slideNumber.setAttribute('max', myVideo.duration);

  
}

