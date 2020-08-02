import customers from 'static/js/customers.js'

console.log(customers)
//make first letter capital
function capital(string){
  return string.charAt(0).toUpperCase() + string.slice(1);
}

function listCustomers(personArray) {
  let customerList = document.querySelector("#customer-list");
  //console.log(customerList);

  for (let customer of customers) {
    let newCustomer = document.createElement("div");
    

//Create Text Nodes
    let customerName = document.createTextNode(`${capital(customer.name.title)}. ${capital(customer.name.first)} ${capital(customer.name.last)} `);
    let cAddress = document.createTextNode(`Address: ${customer.location.street} `)
    let cCityState = document.createTextNode(`${capital(customer.location.city)}, ${capital(customer.location.state)} `)
    let cDOB = document.createTextNode(`Birthday: ${customer.dob} `)
    let customerEmail = document.createTextNode(`Email: ${customer.email}`);
    // let customerEmail = document.createElement("email");
    //customerEmail.src = `${customer.email}`;

//create paragraphs; it will NOT run when I put them further down in the code
    let cName = document.createElement("p");
    let email = document.createElement("p");
    let address = document.createElement("p");
    let cCS = document.createElement("P");
    let bday = document.createElement("p");     

    address.classList.add("address", "measure", "lh-copy");
    cName.classList.add("display");
    address.append(cAddress, cCityState);
 
  //create appendChild
    cName.appendChild(customerName);
    email.appendChild(customerEmail);
    address.appendChild(cAddress);
    cCS.appendChild(cCityState);
    bday.appendChild(cDOB);

    newCustomer.append(cName, email, address, cCS, bday);

//image
    let customerImage = document.createElement("img");
    //br-100 makes picture a circle
    customerImage.classList.add("br-100","h4","w3","dib","ba","b--black-05", "pa2");
    
    customerImage.src = `${customer.picture.medium}`;
     //prepend allowed the image to show
    newCustomer.prepend(customerImage);
    newCustomer.classList.add("ph3", "pv3", "bb");

//Name
    //prints EVERYTHING
    customerList.append(newCustomer);

  };
  
};

listCustomers(customers);

