var dictionary;
$.ajax({
    url: "assets/js/spanish.json",
    dataType: "json",
    isLocal: true,
    crossDomain: true,
    async: false,
    global: false,
    success: function(data){
        dictionary = data;
    },
});

function getRandomWord() {
    var rand = dictionary[Math.floor(Math.random() * dictionary.length)];
    return rand;
}

function changeWord() {
    $("#word").hide(0, function() {
        $(this).html(getRandomWord());
    }).fadeIn(600);
    setTimeout("changeWord()", 6000);
}

changeWord();
