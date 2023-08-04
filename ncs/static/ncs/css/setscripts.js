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
    //document.querySelector('#subjectInput').value ='';
    //document.querySelector('#subjectInput').value = option;
    const subject = document.querySelector('#subjectInput');

    //console.log(option);

    if (option === 'other') {
        subject.style.display = 'block';
        subject.value = '';
        subject.required = true;
        //console.log(document.querySelector('#subjectInput').value);
    } else {
        subject.style.display = 'none';
        subject.value = option;
    }
    console.log(subject.value);

    //radio.forEach( element => {
    //    console.log(element.value);
    
    //}); 
}