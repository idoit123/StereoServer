// Shorthand for $( document ).ready()
$(bindButts);

function bindButts(){
    console.log("binding butts");
    $("#submitbutton").click(submitUrl);
    $("#pausebutton").click(togglePlayPause);
    $("#stopbutton").click(stopPlaying);
    
    // Update the current slider value (each time you drag the slider handle)
    let slider = document.getElementById("volumeslider");
    slider.oninput = function () {
        setVolume(this.value);
    }
}

function setVolume(getal){
    console.log("Setting volume to: " + getal);

    data = {action: "volume", volume: getal};
    makePostRequest(data);
}

function stopPlaying(){
    console.log("Closing player");

    data = {action: "stop"};
    makePostRequest(data);
}

function togglePlayPause(){
    console.log("Toggling play/pause");

    data = {action: "toggle"};
    makePostRequest(data);
}

function submitUrl() {
    let url = document.getElementById('urlToSubmit').value;
    console.log(url);

    playSong(url);
}

function playSong(url){
    console.log("Playing url: "+url);
    
    data = { action: "play", url: url};
    makePostRequest(data);
}

function makePostRequest(data){
    $.post("/", data, function (a, b) {
        console.log("Post request called back.");
    });
}