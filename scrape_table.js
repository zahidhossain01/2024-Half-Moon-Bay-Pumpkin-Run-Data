// copied JS Selector from devtools for table selector
let table = document.querySelector("#radix-\\:r7\\:-content-results > div > div > div.w-100.overflow-auto > table");
let rows = Array.from(table.querySelectorAll('tr')).slice(1);

for (row of rows) {
    row_elements = Array.from(row.children).slice(0,12).map(r => r.textContent.trim());
    console.log( row_elements.join(",") );
}