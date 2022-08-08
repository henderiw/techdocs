# javascript requests

## GET with fetch

```
I fetch GET
fetch('http: //api-to-call.com/endpoint').then(response => {
  if (response. ok) {
		// convert response to json
		return response.json();
	} 
	throw new Error('Request failed!');
}, networkError => console.log(networkError.message) // handle errors
).then (jsonResponse => {
	// Code to execute with jsonResponse success
});
```

```
const getSuggestions = () => {
  const wordQuery = inputField.value;
  const endpoint = `${url}${wordQuery}`;
  
  fetch(endpoint, {cache: 'no-cache'}).then(response => {
    if (response.ok) {
      return response.json();
    }
    throw new Error('Request failed!');
  }, networkError => {
    console.log(networkError.message)
  }).then( jsonResponse => {
    //renderRawResponse(jsonResponse)
    renderResponse(jsonResponse)
  })
}
```

## POST with fetch

```
// Information to reach API
const apiKey = '<Your API Key>';
const url = 'https://api.rebrandly.com/v1/links';

// Some page elements
const inputField = document.querySelector('#input');
const shortenButton = document.querySelector('#shorten');
const responseField = document.querySelector('#responseField');

// Asynchronous functions
const shortenUrl = () => {
  const urlToShorten = inputField.value;
  const data = JSON.stringify({destination: urlToShorten});
  
	fetch(url, {
    method: 'POST',
    headers: {
      'Content-type': 'application/json',
      'apikey': apiKey
    },
    body: data
  }).then(response => {
    if (response.ok) {
      return response.json();
    }
    throw new Error('Request failed!');
  }, networkError => {
    console.log(networkError.message)
  }).then(jsonResponse => {
    renderResponse(jsonResponse)
  })
}

// Clear page and call Asynchronous functions
const displayShortUrl = (event) => {
  event.preventDefault();
  while(responseField.firstChild){
    responseField.removeChild(responseField.firstChild);
  }
  shortenUrl();
}

shortenButton.addEventListener('click', displayShortUrl);
```

## async get

```
const getData = async () => {
	try {
		const tosponse = await fetch/'https://apl-to-call.com/endpoint'l:
		if (response. ok) {
			const jsonResponse = await response.json();
			// code to execute with jsonResponse
		}
		throw new Error( 'Request failed!');
	} catch (error) {
		console.log(error);
	}
}
```

```
// Information to reach API
const url = 'https://api.datamuse.com/words?';
const queryParams = 'rel_jja=';

// Selecting page elements
const inputField = document.querySelector('#input');
const submit = document.querySelector('#submit');
const responseField = document.querySelector('#responseField');

// Asynchronous function
// Code goes here
const getSuggestions = async () => {
  const wordQuery = inputField.value
  const endpoint = url + queryParams + wordQuery
  try {
    const response = await fetch(endpoint, {cache:  'no-cache'})
    if (response.ok) {
      const jsonResponse = await response.json();
      renderResponse(jsonResponse)
    }
  } catch (error) {
		console.log(error);
	}
}


// Clear previous results and display results to webpage
const displaySuggestions = (event) => {
  event.preventDefault();
  while(responseField.firstChild){
    responseField.removeChild(responseField.firstChild)
  }
  getSuggestions();
}

submit.addEventListener('click', displaySuggestions);
```

## async POST

```
// information to reach API
const apiKey = 'jVA0UPneeKGs55CE2kuvCOtdvSii0R85';
const url = 'https://api.rebrandly.com/v1/links';

// Some page elements
const inputField = document.querySelector('#input');
const shortenButton = document.querySelector('#shorten');
const responseField = document.querySelector('#responseField');

// Asynchronous functions
const shortenUrl = async () => {
	const urlToShorten = inputField.value;
  const data = JSON.stringify({destination: urlToShorten});
  try {
    const response = await fetch(url, 
      {
        method: 'POST',
        body: data,
        headers: {
          'Content-type': 'application/json',
          'apikey': apiKey
        }
      }
    );
		if(response.ok){
      const jsonResponse = await response.json();
      renderResponse(jsonResponse);
    }
  } catch (error) {
    console.log(error);
  }
}

// Clear page and call Asynchronous functions
const displayShortUrl = (event) => {
  event.preventDefault();
  while(responseField.firstChild){
    responseField.removeChild(responseField.firstChild);
  }
  shortenUrl();
}

shortenButton.addEventListener('click', displayShortUrl);

```