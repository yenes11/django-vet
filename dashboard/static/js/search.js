const searchField = document.querySelector("#searchField");
const searchPets = document.querySelector(".search-pets")
const listPets = document.querySelector(".list-pets");
const listItem = document.querySelector(".list-item");
const noResult = document.querySelector(".no-result");

searchPets.style.display = "none";
noResult.style.display = "none";

searchField.addEventListener("keyup", (e) => {
    const searchValue = e.target.value;
    noResult.style.display = "none";
    if(searchValue.trim().length > 0){
        listPets.style.display = "none";

        fetch("/search", {  
            body: JSON.stringify({searchText: searchValue}),
            method: "POST",
        })
        .then((res) => res.json())
        .then((data) => {
            console.log(data);

            listPets.style.display = "none";
            searchPets.style.display = "block";

            if(data.length == 0){
                searchPets.style.display = "none";
                noResult.style.display = "block";
            }
            else{
                listItem.innerHTML = "";
                data.forEach((item) => {
                    
                    listItem.innerHTML += `
                        <a href="#" class="list-group-item list-group-item-action flex-column align-items-start">
                            <div class="d-flex w-100 justify-content-between">
                                <h5 class="mb-1">${item.name}</h5>
                                <small></small>
                            </div>
                            <p class="mb-1">${item.description}</p>
                            <small>${item.owner}</small>
                        </a>
                    `;
                });
            }

        });
    }
    else{
        listPets.style.display = "block";
        searchPets.style.display = "none";
    }
});