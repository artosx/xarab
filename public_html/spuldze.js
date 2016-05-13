function spuldze() {
        var x = document.getElementById("myImage");   
        if(x.src.match("bulbon")) {
                x.src = "pic_bulboff.gif";
        } else {
                x.src = "pic_bulbon.gif";
        }
}

