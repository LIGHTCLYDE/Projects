//Class navbardark

const header = document.querySelector('.navbar');

window.onscroll = function() {
    var top = window.scrollY;
    if(top >= 100) {
        header.classList.add('navbarDark');
    }

    else {
        header.classList.remove('navbarDark');
    }
}


// Class form

const button = document.querySelector('button');

    function addLoading() {
    button.innerHTML = '<img src="./images/loading.png" class="loading">';
}

    function removeLoading() {
    button.innerHTML = 'Me contate';
}


const handleSubmit = (event) => {
    event.preventDefault();
    addLoading();

    const name = document.querySelector('input[name=name').value;
    const email = document.querySelector('input[name=email').value;
    


    fetch('https://api.sheetmonkey.io/form/ot4cgXrEwMqEh2sGAdFr16', {

        method: 'post',
        headers: {
            'Accept': 'application/json',
            'Content-type': 'application/json',
        },
        body: JSON.stringify({ name, email }),
    }).then(() => removeLoading(window.location.href = './form_end.html'));
}

document.querySelector('form').addEventListener('submit', handleSubmit);
