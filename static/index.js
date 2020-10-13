document.addEventListener('submit',e=>{
	let mail = document.forms["myform"]["email"].value;
	let pwd = document.forms["myForm"]["password"].value;
	let passw = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&.])[A-Za-z\d$@$!%*?&.]{6, 20}/;
  	let cmail = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/

  	var m=0;
  	if(!cmail.test(mail))
  	{
  		document.getElementsById('mail-log').innerHTML = "Enter a valid email";
  		m=1;
  	}
  	else
  	{
  		document.getElementsById('mail-log').innerHTML = "";
  	}

  	if(!passw.test(pwd))
  	{
  		document.getElementsById("password-log").innerHTML = "Password should contain atleast one [A-Z],[a-z],[1-0],special characters.";
  		m=1
  	}
  	else
  	{
  		document.getElementsById('paswword-log').innerHTML = "";
  	}
  	if(m!=0)
  	{
  		e.preventDeffault();
  	}
  	else
  	{
  		return true;
  	}
});