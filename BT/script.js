function readURL(input) { 
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        
        reader.onload = function (e) {
            $('#blah').attr('src', e.target.result);
        }
     
        reader.readAsDataURL(input.files[0]);
    }
}
$("#imgInp").change(function(){
    readURL(this);
});   

var selectedRow = null;
function onFormSubmit() {
    if (validate()) { 
       var formData = readFormData();
        if (selectedRow == null)
            insertNewRecord(formData);
        else
            updateRecord(formData);
            getData();
        resetForm();
    } 
}


function readFormData() { 
    var formData = {};
    formData["itemName"] = document.getElementById("itemName").value;
    formData["category"] = document.getElementById("category").value;
    formData["imgInp"] =   document.getElementById("imgInp").value ;
    formData["src"]=document.getElementById("blah").src;
    return formData;
}

function insertNewRecord(data) {
    var table = document.getElementById("List").getElementsByTagName('tbody')[0];
    var newRow = table.insertRow( );
    cell0=newRow.insertCell(0);
    cell0.innerHTML = table.rows.length;

    cell1 = newRow.insertCell(1);
    cell1.innerHTML = data.itemName;

    cell2 = newRow.insertCell(2);
    cell2.innerHTML = data.category;

    cell3 = newRow.insertCell(3); 
    cell3.innerHTML="<img src="+document.getElementById("blah").src +">";
    cell4 = newRow.insertCell(4);
    cell4.innerHTML = `<button class="Edit" onClick="onEdit(this)">Edit</button>
                       <button class="Delete" onClick="onDelete(this)">Delete</button>`;

   
}

let arr=[];
function getData()
{
    let data = 
      {
          name:  document.getElementById("itemName").value,
          category : document.getElementById("category").value,
          url :document.getElementById("blah").src,
      }
    arr.push(data);
    let myobj = JSON.stringify(data);
    localStorage.setItem(arr.length.toString(),myobj);
    console.log(myobj);
}

function loadData()
{
  for (let i = 0; i < localStorage.length; i++)
  {
    arr.push(JSON.parse(localStorage.getItem(localStorage.key(i))));
  }
    var table = document.getElementById("List").getElementsByTagName('tbody')[0];
  for(let i=0;i<arr.length;i++)
  {    

      let newRow = table.insertRow(table.length);
      cell0=newRow.insertCell(0);
      cell0.innerHTML = i+1;

      cell1 = newRow.insertCell(1);
      cell1.innerHTML = arr[i].name;

      cell2 = newRow.insertCell(2);
      cell2.innerHTML = arr[i].category;

      cell3 = newRow.insertCell(3);
      cell3.innerHTML = "<img src="+arr[i].url+">";
      cell3.src= document.getElementById("blah").src;
      cell3.value = document.getElementById("imgInp").value;
      cell4 = newRow.insertCell(4);
      cell4.innerHTML = `
                        <input onclick="onEdit(this)" type="button" class="Edit" value="Edit" id="btn_Edit"></input>
                        <input onclick="onDelete(this)" type="button"class="Delete" value="Delete" id="btn_Delete"></input>`;
      }

  }
function validate() {
    isValid = true;
    st="";
    document.getElementById("itemName").value
    if (document.getElementById("itemName").value == "" ) 
    {
        isValid = false;
        document.getElementById("err-name").innerHTML="Name is requỉred";
    } 
    else {
        document.getElementById("err-name").innerHTML="";

    }
    if (document.getElementById("category").value=="No Selected")
    {
        isValid = false;
        document.getElementById("err-category").innerHTML="Category is required";
    }
    else{
        document.getElementById("err-category").innerHTML="";

    }
    if( document.getElementById("imgInp").files.length == 0 )
    { isValid=false;
      document.getElementById("err-file").innerHTML=" * No file selected";
    }
    else{
        document.getElementById("err-file").innerHTML="";

    }
    return isValid;
}
function onEdit(td) {
    selectedRow = td.parentElement.parentElement;
    document.getElementById("itemName").value = selectedRow.cells[1].innerHTML;
    document.getElementById("category").value = selectedRow.cells[2].innerHTML;
   // document.getElementById("imgInp").value= selectedRow.cells[3].files;
    document.getElementById("blah").src=selectedRow.cells[3].firstChild.src;
}
function updateRecord(formData) {
    selectedRow.cells[1].innerHTML = formData.itemName;
    selectedRow.cells[2].innerHTML = formData.category;
    selectedRow.cells[3].innerHTML = "<img src="+formData.src +">";
    getData();
}
function onDelete(td) {
    if (confirm('Are you sure to delete this record ?')) {
        row = td.parentElement.parentElement;
        document.getElementById("List").deleteRow(row.rowIndex);
        
        resetForm();
    }
}

function resetForm() {
    document.getElementById("itemName").value = "";
    document.getElementById("category").value = "";
    document.getElementById("blah").src ="";
    document.getElementById("imgInp").value="";
    selectedRow = null;
} 
