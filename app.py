<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width,height=device-height,initial-scale=1.0"/>
<link href='https://fonts.googleapis.com/css?family=Architects Daughter' rel='stylesheet'>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>

.fa {
  padding: 20px;
  font-size: 30px;
  width: 50px;
  text-align: center;
  text-decoration: none;
  margin: 5px 2px;
}

.fa:hover {
    opacity: 0.7;
}

.fa-facebook {
  background: #3B5998;
  color: white;
}

.fa-twitter {
  background: #55ACEE;
  color: white;
}

.fa-google {
  background: #dd4b39;
  color: white;
}

.fa-youtube {
  background: #bb0000;
  color: white;
}

* {
  box-sizing: border-box;
}

body {
  font-family: Arial;
  padding: 10px;
  background: #f1f1f1;
}
.tri {
	width: 0;
	height: 0;
	border-top: 25px solid transparent;
	border-left: 50px solid #474e5d  ;
	border-bottom: 25px solid transparent;
	margin-left:50%;
	position:relative;
	left:0;
	transition:right ease 20.0s ;
	color:#474e5d;

}

.tri:hover {
border-bottom: 25px solid orange;
border-left: 50px solid orange;
}

/* Header/Blog Title */
.header {
  padding: 30px;
  text-align: center;
  background: white;
  overflow:hidden;
}

.header h1 {
  font-size: 50px;
}

/* Style the top navigation bar */
.topnav {
  background-color: #333;
}

/* Style the topnav links */
.topnav a {

  display:grid;
  color: #f2f2f2;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

/* Change color on hover */
.topnav a:hover {
  background-color: #ddd;
  color: black;
}

/* Create two unequal columns that floats next to each other */
/* Left column */
.leftcolumn {
  float: left;
  width: 75%;
  font-family:'Architects Daughter';
  font-size:18px;
}

/* Right column */
.rightcolumn {
  float: left;
  width: 25%;
  background-color:#f1f1f1  ;
  padding-left: 20px;
  max-height:100%;

}

/* Fake image */
.fakeimg {

  width:95%;
  padding: 20px;
  max-height:auto;
  overflow:hidden;
  background-color:#474e5d;
  border-radius:5%;
  overflow:hidden;

}

/* Add a card effect for articles */
.card {
  background-color:#f1f1f1;
  margin-top: 20px;
  font-family:'Architects Daughter';
  font-size:15px ;
}

.cardx{
  background-color: white;
  padding: 20px;
  margin-top: 20px;
  border-top-right-radius:10%;
  border-bottom-left-radius:10%;
  font-family:'Architects Daughter';
  font-size:15px ;
}

.cardz{
  background-color: whitesmoke;
  padding: 20px;
  margin-top: 20px;
  font-family:'Architects Daughter';
  font-size:18px ;
}

#pork{
  background-color:#f1f1f1;
  padding: 20px;
  margin-top: 20px;
}



#chicken {
  background-color:474e5d;
  padding: 20px;
  margin-top: 20px;
  font-family:'Architects Daughter';
  font-size:18px ;

}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}

.clearfix{
  background-color:#f1f1f1;
  color:#474e5d;
  font-family:'Architects Daughter';
  font-size:18px ;
  }


/* Footer */
.footer {
  padding: 20px;
  text-align: center;
  background: #474e5d;
  margin-top: 20px;
  color:orange;
}

/* Responsive layout - when the screen is less than 800px wide, make the two columns stack on top of each other instead of next to each other */
@media screen and (max-width: 800px) {
  .leftcolumn, .rightcolumn ,  .card, .cardx , .row, .fakeimg {
    width: 100%;
    padding: 0;
  }
}

/* Responsive layout - when the screen is less than 400px wide, make the navigation links stack on top of each other instead of next to each other */

/* Image Gallery */


.row > .column {
  padding: 0 8px;
}

.row:after {
  content: "";
  display: table;
  clear: both;
}

.column {
  float: left;
  width:50%;
  height:auto;
  overflow:hidden;

}

/* The Modal (background) */
.modal {
  display: none;
  position: fixed;
  z-index: 1;
  padding-top: 100px;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color:white;
  opacity:30;
}

/* Modal Content */
.modal-content {
  position: relative;
  background-color: #fefefe;
  margin: auto;
  padding: 0;
  width: 90%;
  max-width: 1200px;

}

/* The Close Button */
.close {
  color: white;
  position: absolute;
  top: 10px;
  right: 25px;
  font-size: 35px;
  font-weight: bold;
}

.close:hover,
.close:focus {
  color: #999;
  text-decoration: none;
  cursor: pointer;
}

.mySlides {
  display: none;
}

.cursor {
  cursor: pointer;
}

/* Next & previous buttons */
.prev,
.next {
  cursor: pointer;
  position: absolute;
  top: 50%;
  width: auto;
  padding: 16px;
  margin-top: -50px;
  color: white;
  font-weight: bold;
  font-size: 20px;
  transition: 0.6s ease;
  border-radius: 0 3px 3px 0;
  user-select: none;
  -webkit-user-select: none;
}

/* Position the "next button" to the right */
.next {
  right: 0;
  border-radius: 3px 0 0 3px;
}

/* On hover, add a black background color with a little bit see-through */
.prev:hover,
.next:hover {
  background-color: rgba(0, 0, 0, 0.8);
}

/* Number text (1/3 etc) */
.numbertext {
  color: #f2f2f2;
  font-size: 12px;
  padding: 8px 12px;
  position: absolute;
  top: 0;
}

img {
  margin-bottom: -4px;
}

.caption-container {
  text-align: center;
  background-color: black;
  padding: 2px 16px;
  color: white;
}

.demo {
  opacity: 0.6;
}

.active,
.demo:hover {
  opacity: 1;
}

img.hover-shadow {
  transition: 0.3s;
}

.hover-shadow:hover {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}


/* End  Of Image Gallery */

.stylock {
color:#474e5d;
font-family: 'Architects Daughter';font-size: 22px;
text-align:center;
}

.official {
max-height:100vw;
max-width:100vw;

}

.aboutplay{
font-family:courier;
}

.sbt {
background-color:green ;
color:white ;
width:170px ;
height:35px;
float:left;
font-style:bold;
font-size:100%;
border:3px solid white;
text-align:center;
margin:0;
display:block;
}


.sbx {
background-color:green ;
color:white ;
width:170px ;
height:35px;
float:right;
font-style:bold;
font-size:100%;
border:3px solid white;
text-align:center;
margin:0;
display:block;
}


.drp{
background-color:green;
color:white;
width:20vw ;
height:3vw;
border:3px solid white;
font-style:bold;
font-size:100%;
margin-left:30%;
}

.drp:hover {
background-color:white;
color:black;
}


.iconics {

margin-left:40%;
}

#div1 {
  font-size:48px;
  float:right;
  color:orange;
}

#div1:hover{
color:cyan;
}

.container {
 padding:2px;
 border:2px solid lightgreen;
 height:30vw;
 max-width:100%;
 text-align:center;
 color:green;
 background-color:whitesmoke;

}

.conta {
 padding:2px;
 height:100%;
 max-width:100%;
 text-align:center;
 color:#474e5d;
 background-color:whitesmoke;
 padding:3px;
 overflow:hidden;
 border-bottom-left-radius:10%;
 border-top-right-radius:10%;
}

.inf {
width:100% ;
height:40px;
border:2px solid #f1f1f1 ;
}


.balance{
color:orange;
}

.aboutplay{
text-decoration:none;
}


table {
  border-collapse: collapse;
  border-spacing: 0;
  width: 100%;
  border: 1px solid #ddd;
  background-color:#474e5d;
}

th, td {
  text-align: left;
  padding: 8px;
  background-color:#80ced6;
}

tr:nth-child(even){background-color:whitesmoke}



.topnav {
  overflow: hidden;
  background-color: #474e5d;

}

.topnav a {
  float: left;
  display: block;
  color:orange;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
}

.active {
  background-color:dodgerblue;
  color: white;
}

.topnav .icon {
  display: none;
}

.dropdown {
  float: left;
  overflow: hidden;
  color:orange;
}

.dropdown .dropbtn {
  font-size: 14px;
  border: none;
  outline: none;
  color:orange;
  padding: 14px 16px;
  background-color: inherit;
  font-family: inherit;
  margin: 0;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #474e5d;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

.dropdown-content a {
  float: none;
  color:orange;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
  text-align: left;
}

.topnav a:hover, .dropdown:hover .dropbtn {
  background-color: #f1f1f1;
  color:black;
}

.dropdown-content a:hover {
  background-color: #f1f1f1;
  color: black;
}

.dropdown:hover .dropdown-content {
  color:#474e5d;
}

.zshi{
float:left;
border-radius:10%;
border:3px solid white ;
}

.porkwrap{
float:right;
border-radius:10%;
border:3px solid white;
}

.btmlink {
color:orange;
text-decoration:none;
}

.overfooter {
border-radius:25px;
text-align:center;
color:orange;
background-color:#474e5d;
}



/*### Smartphones (portrait and landscape)(small)### */
@media screen and (min-width : 0px) and (max-width : 767px){
.card , .cardx { display : stack }
.cardz { text-align:center }
.overfooter { text-align :left  ; font-size:10px ;}
}


.header{
  width:40%;
  height: 100px;
  background-color: red;
  position: relative;
  animation: myfirst 5s linear 2s infinite alternate;
  overflow:hidden;
}

#magic{
float:left;
margin-left:50px;
font-size:40px;
}


#magic2{
float:right;
margin-right:50px;
font-size:40px;
}



@keyframes myfirst {
  0%   {background-color:red; left:0px;  border-radius:20%}
  15%  {background-color:dodgerblue; left:150px; top:0px; bottom:30px ;}
  35%  {background-color:red ; left:100px ; border-radius:40%;color:white}
  55%  {background-color:dodgerblue; left:150px ;  bottom:30px ;}
  75% {background-color:red ; left:150px ; border-radius:50% ; color:white}
  100% {background-color:dodgerblue ; right:150px; border-radius:20% ;}


}



.navbar {
  overflow: hidden;
  background-color:#474e5d;
}

.navbar a {
  float: left;
  font-size: 16px;
  color:orange;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

.dropdown {
  float: left;
  overflow: hidden;
}

.dropdown .dropbtn {
  font-size: 16px;
  border: none;
  outline: none;
  color:orange;
  padding: 14px 16px;
  background-color: inherit;
  font-family: inherit;
  margin: 0;
}

.navbar a:hover, .dropdown:hover .dropbtn {
  background-color:inherit;
  color:white;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #474e5d;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
  color:white;
}

.dropdown-content a {
  float: none;
  color: orange;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
  text-align: left;
}

.dropdown-content a:hover {
  background-color:darkgrey;
  color:white;
}

.dropdown:hover .dropdown-content {
  display: block;
}
</style>
</head>
<body>

<div class="header">

<h3> KYLENATH ENTERPRISES </h3>
</div>

<div class="topnav" id="myTopnav">


<div class="navbar">
  <a href="#home" style="float:right"><i class="fa fa-sign-in" style="font-size:28px"></i> Register  </a>
  <a href="#news" style="float:right"><i class="fa fa-user-circle-o" aria-hidden="true"></i>Log in  </a>
   <a href="{{url_for("order")}}" style="float:right"> <i class="fa fa-shopping-cart" aria-hidden="true"></i>Buy Products </a>
  <div class="dropdown" style="float:left"  >
    <button class="dropbtn">Products
      <i class="fa fa-caret-down"></i>
    </button>
    <div class="dropdown-content">
     <a href="#pork">Pig Section</a>
      <a href="#chicken">Chicken Section </a>
      <a href="{{url_for("finisher")}}"> Beef & Sheep </a>
    </div>
  </div>
</div>
  </div>
</div>

<div class="row">
  <div class="leftcolumn">
    <div id="chicken">
    <h2 class="stylock">KYLENATH ENTERPRISE </h2>
    <p class="stylock" style="font-size:18px"> We are a Digitalised Farming Community dealing in a wide range of products mainly listed below </p>
    <ol class="stylock" style="font-size:18px">
    <li> Pork (Pig) </li>
    <li> Chicken </li>
    <li> Mutton(Sheep) </li>
    <li> Beef </li>
    </ol>
    <p class="stylock" style="font-size:18px"> All of our products are health certified and genuinly bear stamp to ensure a clean , healthy and non - contaminated meat supply
    We sell both live and slaughtered products with respect to customers orders . Orders once activated can be collected within 24-48 hrs </br>  Depending on the region of purchase . Closer Regions will experience faster ddrio </p>
      <h2 class="stylock">KYLENATH CHICKEN PRODUCTION SITE </h2>
      <h5 class="stylock" >CHICKEN BREEDS  </h5>

      <ol  class="stylock" style="font-size:18px; text-align:left">
      <li> Kienyeji --<i> Traditional Chicken </i> -- </li>
      <li> Improved Kienyeji --<i> Interlocal Chicken </i> --</li>
      </ol>
        <h5 class="stylock">CHICKEN PRODUCTS</h5>
    <div style="overflow-x:auto;">
    </div>


      <div class="fakeimg" style="overflow:scroll">
      <div class="row">
  <div class="column" >
    <img style="official" src="{{url_for('static' , filename='images/chicken/' + 'chick1.jpg')}}" onclick="openModal();currentSlide(1)" class="hover-shadow cursor">
  </div>
    <div class="column">
    <img style="official" src="{{url_for('static' , filename='images/chicken/' + 'cd.jpg')}}" onclick="openModal();currentSlide(2)" class="hover-shadow cursor">
  </div>
  <div class="column">

  </div>

</div>

<div id="myModal" class="modal">
  <span class="close cursor" onclick="closeModal()">&times;</span>
  <div class="modal-content">
{% for image_name in image_name %}
    <div class="mySlides">
      <div class="numbertext">{{image_count -defactor }} / 4</div>
      <img src="{{url_for('static' , filename='images/chicken/' + image_name )}}" style="width:100%">
    </div>
{% endfor %}


    <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
    <a class="next" onclick="plusSlides(1)">&#10095;</a>

    <div class="caption-container">
      <p id="caption"></p>
    </div>
  </div>
</div>

      </div>
      <div class="clearfix">


      <p class="shift">
      <img class="zshi" src="{{url_for('static' , filename="chicken.gif")}}" style="height:280px; width:45% ;">&nbsp &nbsp Kylenath Enterprises Offers You A Quick And Reliable Meat (Chicken) Supply  , </br> &nbsp &nbsp Retrieved From the Best chosen Animals  We are confident that youll love it .&nbsp &nbsp In addition , Our Meat is also Health insured and bears the Regional Stamp Of Health Board And Regulations </br> &nbsp &nbsp  For More Info On this Product Click the link Below

      </p>
     <i id="magic" class="fa fa-shopping-cart"></i>
     <i id="magic2" class="fa fa-info" ></i>
      </br>
      </br>


    </div>
    </div>
    <div id="pork">
      <h2 class="stylock"  > KYLENATH PORK </h2>
      <h5 class="stylock" >Pork Products </h5>
      <div class="fakeimg" style="overflow:scroll">
      <div class="row">
  <div class="column">
    <img style="official" src="{{url_for('static' , filename='images/pigs/' + 'pig.jpg')}}" onclick="xopenModal();currentSlide(1)" class="hover-shadow cursor">
  </div>
    <div class="column">
    <img style="official" src="{{url_for('static' , filename='images/pigs/' + 'pig1.jpg')}}" onclick="xopenModal();currentSlide(1)" class="hover-shadow cursor">
  </div>

</div>
      </div>
      <div id="xModal" class="modal">
  <span class="close cursor" onclick="xcloseModal()">&times;</span>
  <div class="modal-content">
{% for pig_image in pig_image %}
    <div class="mySlides">
      <div class="numbertext">{{pig_count - defactor }} / 4</div>
      <img src="{{url_for('static' , filename='images/pigs/' + pig_image )}}" style="width:100%">
    </div>
{% endfor %}


    <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
    <a class="next" onclick="plusSlides(1)">&#10095;</a>

    <div class="caption-container">
      <p id="caption"></p>
    </div>


  </div>
</div>
      <div class="clearfix">
      </br>
      </br>
       <h3> &nbsp &nbsp Pork Products </h3>
       <p>
      <img class="porkwrap" src="{{url_for('static' , filename="piganime.gif")}}" style="height:280px; width:45% ;">&nbsp &nbsp We at {{ webtitle }}  also focus on Pork production at a large scale level ,&nbsp From Live Animal Sells To Desired Meat CHops We Got You Covered <br>  &nbsp &nbsp Currently Available Breeds Have Been Listed Below  </br>
      <ol>
      <li> Large Duroc White </li>
      <li> Berkshire </li>
      <li> Other Breed (On Demand) </li>
      </ol>
    Make An Order ?  For More Info On this Product Click the link Below !
      <p>
      <i id="magic" class="fa fa-shopping-cart"><a href="{{url_for("order")}}" > </a> </i>
     <i id="magic"  class="fa fa-info"  ></i>
     </br>
     </p>
     </br>
      <h3 class="stylock" style="text-align:center ; color:orange "> <b> Next Page </b> </h3>
      <a href="{{url_for('finisher')}}" > <div class="tri"></div> </a>
      </br>
      </br>
      </br>
      </p>
    </div>
    </div>
  </div>


  <div class="rightcolumn">

    <div class="card" style="background-color:#f1f1f1" >
      <h2><marquee direction="up"  >Kylenath Enterprises </marquee></h2>
      <div class="fakeimg" style="height:auto;">
      <img style="max-width:100% ; max-height:100% " src="{{url_for('static' , filename='images/logo/' + 'logo.png')}}">
      </div>
      <h4 class="aboutplay"> <a href="{{url_for("about")}}" class="aboutplay"  >  &nbsp &nbsp Visit Our About Page </a></h4>
    </div>
    <div class="card">
    <h3 class="aboutplay" style="text-align:center ; color:orange"> Quick Links </h3>
     <a href="{{url_for("finisher")}}">
      <img class="iconics" src="https://img.icons8.com/ios-glyphs/30/000000/bull.png"/>
    </a>
      </br>
      </br>
      </br>
      <a href="#chicken">
      <img class="iconics" src="https://img.icons8.com/metro/30/000000/chicken.png"/>
    </a>
      </br>
      </br>
      </br>

       <a href="{{url_for("finisher")}}">
      <img class="iconics" src="https://img.icons8.com/ios-filled/50/000000/sheep2.png"/>
      </a>
      </a>
      </br>
      </br>
      </br>
        <a href="#pork">
      <img class="iconics"  src="https://img.icons8.com/android/50/000000/pig.png"/>
    </a>
      </br>
      </br>
      </br>
    </div>
    <div class="cardz">
      <h3> &nbsp &nbsp &nbsp &nbsp  Follow Us On </h3>
      <a href="#" class="fa fa-facebook"></a>
<a href="#" class="fa fa-twitter"></a>
<a href="#" class="fa fa-google"></a>
<a href="#" class="fa fa-youtube"></a>
</div>
<div class="cardx" style="background-color:#474e5d; border:2px solid #474e5ds">
<div class="conta">
    <b> <h4>Please Subscribe to our Newsletter</h4> </b>
    <label style="float:left">&nbsp  Username </label>
    </br>
    <input style="float:left" class="inf" type="text" placeholder=" &nbsp Enter Username" name="mail" required></input>
    </br>
      </br>
      </br>
    <label style="float:left"> &nbsp Email Address </label>
      </br>
    <input style="float:left" class="inf" type="email" placeholder="&nbsp Enter Email address" name="mail" required></input>
    </br>
    </br>
      </br>

      <input type="checkbox" checked="checked" name="subscribe">Terms And Conditions </input>
      </br>
      </br>
      <button class="sbt" style="margin-left:30px"> Accept </button>

  </div>
</div>
    </div>
  </div>
</div>
</div>
<div class="footer">
<div class="footer">
<div class="overfooter">
<p style="color:white ; font-size:20px ; text-align:center; color:orange;"  <b> <marquee> KYLENATH ENTERPRISES </marquee> </b> </p>
<a class="btmlink" href="{{url_for("finisher")}}" style="float:left; margin-left:30px ;" > Product Pricing </a></br>
<a class="btmlink" href="{{url_for("finisher")}}" style="float:left; margin-left:30px ;" > About Us </a></br>
<a class="btmlink" href="{{url_for("finisher")}}" style="float:left; margin-left:30px ;" > Farm Locations </a></br>
<a class="btmlink" href="#pork" style="float:right; margin-right:30px ;" > Pig </a></br>
<a class="btmlink" href="#chicken" style="float:right; margin-right:30px ;" > Chicken </a></br>
<a class="btmlink" href="{{url_for("finisher")}}" style="float:right; margin-right:30px ;" > Beef </a></br>
<a class="btmlink" href="{{url_for("finisher")}}" style="float:right; margin-right:30px ;" > Sheep </a></br>






  <p style="text-align:center">
  Copyright 2020  | Designed By <a href="" > G.A.S.A </a>
  </p>
  </div>
</div>

</div>

</body>
<script>
function openModal() {
  document.getElementById("myModal").style.display = "block";
}

function closeModal() {
  document.getElementById("myModal").style.display = "none";
}
function xopenModal() {
  document.getElementById("xModal").style.display = "block";
}

function xcloseModal() {
  document.getElementById("xModal").style.display = "none";
}


var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}


function myFunction() {
  var x = document.getElementById("myTopnav");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}

function weightConverter(valNum) {
  document.getElementById("scaleout").innerHTML=valNum*400 + "/=";
}

var slideIndex = 0;
showSlides();

function showSlides() {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
  setTimeout(showSlides, 2000); // Change image every 2 seconds
}


function smile() {
  var a;
  a = document.getElementById("div1");
  a.innerHTML = "&#xf118;";
  setTimeout(function () {
      a.innerHTML = "&#xf11a;";
    }, 1000);
  setTimeout(function () {
      a.innerHTML = "&#xf119;";
    }, 2000);
  setTimeout(function () {
      a.innerHTML = "&#xf11a;";
    }, 3000);
}
smile();
setInterval(smile, 4000);


</script>
</html>
