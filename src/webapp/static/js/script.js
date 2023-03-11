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


function updateInfos() {
  var infos = document.getElementById('video-duration-info');
  var slideControl = document.getElementById('slide-control');
  slideControl.style.display = 'block';
  infos.textContent = `Your video has a duration of ${myVideo.duration} seconds.`;
  var slideNumber = document.getElementById('slide-number');
  console.log(slideNumber);
  slideNumber.setAttribute('max', myVideo.duration);

  
}

