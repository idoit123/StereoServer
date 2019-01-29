// Shorthand for $( document ).ready()
$(bindButts);

function bindButts(){
    console.log("binding butts");
    $("#submitbutton").click(submitUrl);
    $("#pausebutton").click(togglePlayPause);
    var slider = document.getElementById("volumeslider");
    // Update the current slider value (each time you drag the slider handle)
    slider.oninput = function () {
        setVolume(this.value);
    }
}

function submitUrl(){
    let url = document.getElementById('urlToSubmit').value;
    console.log(url);

    playSong(url);
}

function setVolume(getal){
    console.log("Setting volume to: " + getal);

    data = {
        action: "volume",
        volume: getal
    };

    makePostRequest(data);
}

function togglePlayPause(){
    console.log("toggling play/pause");

    data = {
        action: "toggle"
    };

    makePostRequest(data);
}

function playSong(url){
    console.log("playing url: "+url);
    
    data = {
        action: "play",
        url: url
    };

    makePostRequest(data);
}

function makePostRequest(data){
    $.post("/", data, function (a, b) {
        console.log("called back.");
    });
}