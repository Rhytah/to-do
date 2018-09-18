//show signup when button is clicked            
function show(id) {
var e = document.getElementById(id);
if(e.style.display == 'none')
e.style.display = 'block';
else
e.style.display = 'none';
}
//hide login
function hide(id) {
  var d = document.getElementById(id);
  if(d.style.display == 'block')
  d.style.display ='none';
  else
  d.style.display='block';
}

//signup message 
function singupAlert(){
    alert("Sign up successful");
}

function sform(a) {
    if (a == 1)
        document.getElementById("SignUp").style.display = "block";
}

// Create a "close" button and append it to each list item
var myNodelist = document.getElementsByTagName("LI");
var i;
for (i = 0; i < myNodelist.length; i++) {
  var span = document.createElement("SPAN");
  var txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  myNodelist[i].appendChild(span);
}

// Click on a close button to hide the current list item
var close = document.getElementsByClassName("close");
var i;
for (i = 0; i < close.length; i++) {
  close[i].onclick = function() {
    var div = this.parentElement;
    div.style.display = "none";
    alert("list item not considered");
  }
}

// Add a "checked" symbol when clicking on a list item
// var list = document.querySelector('ol');
// list.addEventListener('click', function(ev) {
//   if (ev.target.tagName === '') {
//     ev.target.classList.toggle('checked');
//   }
// }, false);

// Create a new list item when clicking on the "Add" button
function newElement() {
  var li = document.createElement("LI");
  var inputValue = document.getElementById("myInput").value;
  var t = document.createTextNode(inputValue);
  li.appendChild(t);
  if (inputValue === '') {
    alert("You must write something!");
  } else {
    document.getElementById("todolist").appendChild(li);
  }
  document.getElementById("myInput").value = "";

  var span = document.createElement("SPAN");
  var txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  li.appendChild(span);

  for (i = 0; i < close.length; i++) {
    close[i].onclick = function() {
      var div = this.parentElement;
      div.style.display = "none";
    }
  }
}
//button clicked to add a new list            
function addlist(a) {
  if (a == 1)
      document.getElementById("todoadd").style.display = "block";
}

// indicate status onclick
function mark(){
  var m = document.getElementById('mark');
  if (m.innerHTML === "Incomplete"){
    m.innerHTML = "Complete";
    
  }else {
    m.innerHTML = "Incomplete";
  }
}

//open tab 
function opentab(evt, tabName ){
  var t, tabcontent, tablink;
  tabcontent=document.getElementsByClassName('tabcontent');
  for(t=0; t< tabcontent.length; t++){
    tabcontent[t].style.display="none";
  }
  tablink =document.getElementsByClassName('tablink');
  for(t=0; t <tablink.length; t++){
    tablink[t].className = tablink[t].className.replace("active ", "");
  }
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += "active";
  
}



//add rows to table
// var  table=document.getElementById('todolist');
// var tr = document.createElement("tr");
// var td = document.createElement("td");