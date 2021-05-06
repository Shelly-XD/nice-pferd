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

}