// JavaScript to toggle the visibility of the table
document.querySelector('.collapsible').addEventListener('click', function() {
    var content = document.querySelector('.collapsible-content');
    content.style.display = (content.style.display === 'none' || content.style.display === '') ? 'block' : 'none';
});
