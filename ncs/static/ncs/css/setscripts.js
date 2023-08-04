document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#subjectInput').style.display = 'none';

    //document.querySelector('#radio').addEventListener('click', () => getradioValue());
    document.querySelector('#inlineRadio1').addEventListener('click', () => getradioValue('Site Survey'));
    document.querySelector('#inlineRadio2').addEventListener('click', () => getradioValue('Intranet'));
    document.querySelector('#inlineRadio3').addEventListener('click', () => getradioValue('Web app'));
    document.querySelector('#inlineRadio4').addEventListener('click', () => getradioValue('ASANKA'));
    document.querySelector('#inlineRadio5').addEventListener('click', () => getradioValue('other'));
    

});

function getradioValue(option) {
    //const radio = document.querySelectorAll('.form-check-input');
    //let radiochecked;

    console.log(option);
    if (option === 'other') {
        document.querySelector('#subjectInput').style.display = 'block';
    } else {
        document.querySelector('#subjectInput').style.display = 'none';
    }
    

    //radio.forEach( element => {
    //    console.log(element.value);
    
    //}); 
}