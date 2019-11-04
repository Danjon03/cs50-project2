document.addEventListener('DOMContentLoaded', () => {
	var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

	socket.on('connect', () => {
    document.querySelector('#submit').onclick = () => {

        const request = new XMLHttpRequest();
        const text = document.querySelector('#text').value;
	};
	
	)};
		

            // Update the result div
            
                const li = document.createElement('li');
				li.innerHTML = `Daniel: ${text}`;
				document.querySelector('#votes').append(li);
            

    
        
    

});
