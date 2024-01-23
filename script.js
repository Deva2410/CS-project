document.getElementById('downloadButton').addEventListener('click', function () {
    // Create a link with a 'download' attribute
    var link = document.createElement('a');
    link.href = 'D:\Los Pollos Hermanos Rentals\main.py'; // Replace with the actual path to your code
    link.download = 'D:\Los Pollos Hermanos Rentals\main.py';

    // Append the link to the document and trigger a click
    document.body.appendChild(link);
    link.click();

    // Remove the link from the document
    document.body.removeChild(link);
});
