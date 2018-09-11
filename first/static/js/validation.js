	function hasNumber(myString) {
	  return /\d/.test(myString);
	}

	function hasUpperCase(str) {
    	return (/[A-Z]/.test(str));
	}

	function validate(){
		var pass = document.getElementById("id_password1").value;
		var cpass = document.getElementById("id_password2").value;

		if(pass.length<8){
			alert("Password must contain at least 8 characters");
			return false;
		}
		else if(!hasNumber(pass))
		{
			alert("Password must contain at least 1 number");
			return false;			
		}
		else if(!hasUpperCase(pass))
		{
			alert("Password must contain at least 1 Capital Letter");
			return false;			
		}
		else if(pass != cpass)
		{
			alert("Password and Password confirmation must be same");
			return false;			
		}

	}
