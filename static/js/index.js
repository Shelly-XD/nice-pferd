function selectionChanged() {
    var e = document.getElementById("selectChapter");
    var value = e.options[e.selectedIndex].value;
    document.getElementById("openReader").style.visibility = "visible";
    document.getElementById("deleteChapter").style.visibility = "visible";
    document.getElementById("readerLink").href = "./scanreader?chapter=" + value;
}

function showMoreShowLess() {
    var moreOptions = document.getElementById("moreOptions");
    var btnText = document.getElementById("showmore");
  
    if (moreOptions.style.display === "none") {
      btnText.innerHTML = "Single Url Download"; 
      moreOptions.style.display = "inline";
      document.getElementById("url").style.display = "none";
    } else {
      btnText.innerHTML = "Multiple URLs Download"; 
      moreOptions.style.display = "none";
      document.getElementById("url").style.display = "inline";
    }
}

function showHideAddManga() {
  var div = document.getElementById("addSerie");
  var divVisibility = div.style.display;

  if (divVisibility === "inline") {
    document.getElementById("addSerie").style.display = "none"
    document.getElementById("addManga").innerHTML = "Show Add Base Url"
  } else {
    document.getElementById("addSerie").style.display = "inline"
    document.getElementById("addManga").innerHTML = "Hide Add Base Url"
  }
}

function addBaseurl() {
  url = "/get?action=addbaseurl&firstUrlSegment=" + document.getElementById("firstUrlSegmentToAdd").value+ "&lastUrlSegment=" + document.getElementById("lastUrlSegmentToAdd").value + "&mangaName=" + document.getElementById("mangaNameToAdd").value;
  $.get(url)
  document.getElementById("firstUrlSegmentToAdd").value = ""  //clear document
  document.getElementById("lastUrlSegmentToAdd").value = ""
  document.getElementById("mangaNameToAdd").value = ""
}

function setBaseUrl () {
  var e = document.getElementById("baseurlSelect");
  var baseurl = eval(e.value);
  mangaId = e.options[e.selectedIndex].text;
  if (moreOptions.style.display === "inline") {
    //Multiple Urls
    document.getElementById("firstUrlSegment").value = baseurl[0];
    document.getElementById("lastUrlSegment").value = baseurl[1];
  } else {
    //single Url
    document.getElementById("url").value = baseurl[0] + "x" + baseurl[1]; 
  }
}

function downloadChapter () {
    var e = document.getElementById("baseurlSelect")
    
    if (document.getElementById("moreOptions").style.display === "inline"){
        console.log("Multiple URLs Download")
        var e = document.getElementById("firstUrlSegment");
        var firstUrlSegment = (e.value);
        var e = document.getElementById("chapterStart");
        var chapterStart = (e.value);
        var e = document.getElementById("chapterEnd");
        var chapterEnd = (e.value);
        var e = document.getElementById("lastUrlSegment");
        var lastUrlSegment = (e.value);

        sendJSON({
          "action":"download",
          "data":{
            "type":"multiple",
            "url1":firstUrlSegment,
            "url2":lastUrlSegment,
            "start":chapterStart,
            "end":chapterEnd,
            "mangaId":mangaId
          }
        },function (data) {
          console.log(data);
        });

        var status = 0
        document.getElementById("progressBar").style.visibility = "visible";
        document.getElementById("buttonsToHide").style.visibility = "hidden";
        updateBar();
        
    } else {
        console.log("singleUrlDownload")
        var e = document.getElementById("url");
        var selectUrl = (e.value);
        if (selectUrl != "") {
            url = "/get?action=download&type=single&url=" + selectUrl + "&mangaId=" + mangaId;
            sendJSON({
              "action":"download",
              "data":{
                "type":"single",
                "url":selectUrl,
                "mangaId":mangaId
              }
            },function (data) {
              console.log(data);
            });

            var status = 0
            document.getElementById("progressBar").style.visibility = "visible";
            document.getElementById("buttonsToHide").style.visibility = "hidden";
            updateBar();
        }
    }
}

function updateBar(){
    var versionUpdate = (new Date()).getTime();
    sendJSON({
      "action":"status",
      "data":{}
    },function (status) {
      console.log(status)
      if (status < 100) {
        document.getElementById("progressBar").value = status;
        setTimeout(() => {  updateBar(); }, 1000);
      } else {
        document.getElementById("progressBar").value = 100;
        setTimeout(() => {  console.log("Download complete"); }, 1000);
        document.getElementById("progressBar").style.visibility = "hidden";
        document.getElementById("buttonsToHide").style.visibility = "visible";
      }
    })
}

function darkmode() {
  document.body.classList.toggle("dark-mode");
  for (var i of document.getElementsByTagName("header")) {
    i.classList.toggle("header-dark-mode")
  }
  for (var i of document.getElementsByTagName("button")) {
    i.classList.toggle("button-dark-mode")
  }
  for (var i of document.getElementsByTagName("a")) {
    i.classList.toggle("a-dark-mode")
  }
  document.getElementById("alerts").classList.toggle("alerts-dark-mode");
  document.getElementById("addManga").classList.toggle("click-dark-mode");
  document.getElementById("showmore").classList.toggle("click-dark-mode");
}

function deleteChapter() {
    var e = document.getElementById("selectChapter");
    var value = e.options[e.selectedIndex].value;
    console.log(value)
    url = "/get?action=delete&id=" + value;
    $.get(url);
}

selectionChanged();
document.getElementById("progressBar").style.visibility = "hidden";
document.getElementById("buttonsToHide").style.visibility = "visible";
document.getElementById("moreOptions").style.display="none"
document.getElementById("addSerie").style.display="none"
var mangaId = ""
