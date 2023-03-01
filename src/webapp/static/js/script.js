const form = document.getElementById("my-form");

form.addEventListener("submit", (e) => {
  e.preventDefault();

  const video = document.getElementById("video-file").files[0];
  const slideTime = document.getElementById("slide-duration").value;

  const formData = new FormData();
  formData.append("video_file", video);
  formData.append("slide_time", slideTime);

  const xhr = new XMLHttpRequest();
  xhr.open("POST", "/upload");
  xhr.onload = () => {
    console.log(xhr.responseText);
  };

  xhr.send(formData);
});
