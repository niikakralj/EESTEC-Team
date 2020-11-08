
function onSucessfulLogin(data,dataName){
if(dataName=="points"){
    $('#userPoints').html(5000);
    //$('#userPoints').html(data.points);
}
if(dataName=="statistics"){
    var table = $('#recycleBinHistory')
    $.each(data, function(idx, elem){
        table.append("<tr bgcolor=\"#FAFAD2\"><td>"+idx+"</td> <td>"+elem.timestamp+"</td><td>"+elem.weight+"</td>   <td>"+elem.bin_type+"</td> <td>"+2500+"</td> </tr>");
    });
}
else{
 
}
}

$(document).ready(function(){
//get points
$.ajax({
        type: "GET",
        url: "http://35.198.189.129:443/smartbin/api/v1/users_bins_data/points" ,
        headers: {
            "accept": "application/json",
        },
        
        success: function(data){onSucessfulLogin(data,"points")},
        error: function(){alert("napaka")},
});

$.ajax({
    type: "GET",
    url: "http://35.198.189.129:443/smartbin/api/v1/users_bins_data/statistics" ,
    headers: {
        "accept": "application/json",
    },
    
    success: function(data){onSucessfulLogin(data,"statistics")},
    error: function(){alert("napaka")},
});




})