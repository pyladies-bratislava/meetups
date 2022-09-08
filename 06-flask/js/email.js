var templateParams = {
    from_name: 'Zuzana',
    message_html: '28.06.2019 at 19:00.',
    from_email: 'your_email@gmail.com',
    phone: '0983628292'
};

emailjs.send('gmail', 'template_2AVmxoMj', templateParams, 'user_j5WmixUTh4jUn51ez4SAn')
    .then(function(response) {
       console.log('SUCCESS!', response.status, response.text);
    }, function(error) {
       console.log('FAILED...', error);
    });