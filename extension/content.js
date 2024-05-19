function postActivity(activity) {
  fetch("http://localhost:5000/activity", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(activity),
  })
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.error("Error:", error));
}

function getVideoInfo() {
  const videoElement = document.querySelector("video");
  if (!videoElement) return null; // Ensure video element exists
  const videoId = new URLSearchParams(window.location.search).get("v");
  const videoAuthorElement = document.querySelector("#channel-name a");
  const videoAuthor = videoAuthorElement
    ? videoAuthorElement.innerText.trim()
    : "Unknown";
  const channelId = videoAuthorElement
    ? new URL(videoAuthorElement.href).pathname.split("/")[2]
    : "Unknown";

  const videoTitleElement = document.querySelector("#below #title h1");
  const videoTitle = videoTitleElement
    ? videoTitleElement.innerText.trim()
    : "Unknown Title";
  const videoDuration = videoElement.duration;
  const currentTimeElapsed = videoElement.currentTime;
  const isPaused = videoElement.paused;
  const url = window.location.href;

  return {
    type: "video",
    videoId: videoId,
    videoTitle: videoTitle,
    videoDuration: videoDuration,
    currentTimeElapsed: currentTimeElapsed,
    videoAuthor: videoAuthor,
    channelId: channelId,
    isPaused: isPaused,
    url: url,
  };
}

function getSearchInfo() {
  const searchInput = document.querySelector("input#search");
  const searchTerm = searchInput ? searchInput.value.trim() : "";
  const url = window.location.href;

  return {
    type: "search",
    searchTerm: searchTerm,
    url: url,
  };
}

function detectActivity() {
  if (window.location.pathname === "/watch") {
    const videoInfo = getVideoInfo();
    if (videoInfo) postActivity(videoInfo);
  } else if (window.location.pathname === "/results") {
    const searchInfo = getSearchInfo();
    if (searchInfo.searchTerm) postActivity(searchInfo);
  } else if (window.location.pathname.startsWith("/shorts/")) {
    postActivity({ type: "shorts", url: window.location.href });
  } else {
    postActivity({ type: "browsing", url: window.location.href });
  }
}

setInterval(detectActivity, 5000);
