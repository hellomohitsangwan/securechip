document.addEventListener('DOMContentLoaded', function () {

    var scrapeButton = document.getElementById('scrapeButton');
    var resultList = document.getElementById('resultList');

    scrapeButton.addEventListener('click', function () {
        isLoading = true;

        chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
 
            chrome.scripting.executeScript({
                target: { tabId: tabs[0].id },
                function: () => {

                    Array.from(document.images).map(img => {

                        var myHeaders = new Headers();
                        myHeaders.append("Content-Type", "application/json");

                        var raw = JSON.stringify({
                            "urls": img.src
                        });

                        var requestOptions = {
                            method: 'POST',
                            headers: myHeaders,
                            body: raw,
                            redirect: 'follow'
                        };
                        fetch("https://flask-production-932e.up.railway.app/urls", requestOptions)
                            .then(response => response.json())
                            .then(data => {
                                console.log(data)
                                console.log(data["obscenity_score"])
                                var score = parseFloat(data["obscenity_score"]);
                                console.log(score)
                                if(score > 0.4){
                                    console.log("gayab started")
                                    img.src = ""
                                    console.log("gayab done")
                                }
                                console.log("Hello1")
                            })
                            .catch(error => console.log('error', error));

                    });


                }
            }, function (result) {
                console.log(result);
            });
        });
    });
});


  
    function displayResults() {
      resultList.innerHTML = '';
      if (isLoading) {
        resultList.innerHTML = '<p>Loading...</p>';
      } else if (error) {
        resultList.innerHTML = '<p>Error: ' + error + '</p>';
      } else {
        urls.forEach(function (url) {
            url.map(u => {
                console.log(u)
                if(u) {
                    var listItem = document.createElement('li');
                    listItem.textContent = u;
                    resultList.appendChild(listItem);
                }

            })

        });
      }
    }

  