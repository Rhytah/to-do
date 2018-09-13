            
function show(id) {
var e = document.getElementById(id);
if(e.style.display == 'none')
e.style.display = 'block';
else
e.style.display = 'none';
}
function singupAlert(){
    alert("Sign up successful");
}

function sform(a) {
    if (a == 1)
        document.getElementById("SignUp").style.display = "block";
}