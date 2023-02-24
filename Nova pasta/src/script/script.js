let docTitle = document.title;
window.addEventListener('blur', () => {
    document.title = 'Volte para ver algumas novidades!';
});

window.addEventListener('focus', () => {
    document.title = docTitle;
});
