document.addEventListener('DOMContentLoaded', function() {
    const localContentLabel = document.querySelector('#local-content-label');
    const localContent = document.querySelector('#local-content');
    const countryListLabel = document.querySelector('#country-list-lebel');
    const countryList = document.querySelector('#country-list');

    const all_close = document.querySelectorAll('.close');
 
    localContentLabel.style.cursor = 'pointer';
    countryListLabel.style.cursor = 'pointer';

    localContentLabel.addEventListener('click', () => {show_element(localContent)});
    countryListLabel.addEventListener('click', () => show_element(countryList));
    
    all_close[0].addEventListener('click', () => close_element(localContent));
    all_close[1].addEventListener('click', () => close_element(countryList));
    //all_close[all_close.length -1].addEventListener('click', () => close_element(countryList));

});

function show_element(element) {
    element.style.display = 'block';
}

function close_element(element) {
    element.style.display = 'none';
}