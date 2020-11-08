
function sucessfulSignIn(){

    alert("Uspešno ste see prijavili");
    
}

function failedSignIN(e){

    alert(e)
}

function signinValidate() {
    var formname='singin'
    //regex for email validation
    var url ="http://35.198.189.129:443/smartbin/api/v1/users/";
    const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    var name = document.forms[formname]["fname"].value;
    var surname = document.forms[formname]["fsurname"].value;
    var email = document.forms[formname]["femail"].value;
    var username = document.forms[formname]["fusername"].value;
    var password = document.forms[formname]["fpassword"].value;
    var confpassword = document.forms[formname]["fconfpassword"].value;
  
    if (name == "" || surname == "" || email == "" || username == "" || password == "" || confpassword =="") {
        alert("You did not fill all the fields.");
        return false;
    }
    else if (!(re.test(email))){
        alert("Email is not valid.");
        return false;
    }
    else if (password != confpassword) {
        alert("Password does not match");
        return false;
    }
    else if (name.length > 16) {
        alert("Your name is too long.");
        return false;
    }
    else if (surname.length > 16) {
        alert("Your surname is too long.");
        return false;
    }
    else if (username.length > 16) {
        alert("Your username is too long.");
        return false;
    }
    else if (password.length < 4) {
        alert("Your password is too short.");
        return false;
    }
    else if (password.length > 16) {
        alert("Your password is too long.");
        return false;
    }
    else{
        
       
      var tosend= {
            "email":email ,
            "name": name,
            "surname": surname,
            "password": password,
            "username": username
          }
          $.ajax({
            type: "POST",
            url: url,
            data: JSON.stringify(tosend),
            headers: {
                "accept": "application/json",   //If your header name has spaces or any other char not appropriate
                "Content-Type": "application/json" //for object property name, use quoted notation shown in second
            },
            
            success: function(){sucessfulSignIn()},
            error: function(){failedSignIN()},
        });
       
    }

}
