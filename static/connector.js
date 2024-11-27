document.getElementById('display-btn').addEventListener('click', displayData)

async function displayData(){

    const dataDisplay = document.getElementById('display_data')    
    dataDisplay.innerHTML = "Loading data..."

    try{
        const response = await fetch('http://127.0.0.1:5000/data')
        if (response.ok){
            console.log('Response Recieved')
            const data = await response.json()
            

            if (Array.isArray(data)){

                const table = document.createElement('table')

                const headerRow = `
                    <thead>

                    <tr>
                            <th>N Level</th>
                            <th>P Level</th>
                            <th>K Level</th>
                            <th>M Level</th>
                            <th>Timestamp</th>
                    </tr>
                    
                    
                    </thead>
                `
                table.innerHTML = headerRow
                const tableBody = document.createElement('tbody')

                data.forEach(item=>{
                    const row = `
                        <tr>
                            <td>${item.N_level.toFixed(2)}</td>
                            <td>${item.P_level.toFixed(2)}</td>
                            <td>${item.K_level.toFixed(2)}</td>
                            <td>${item.M_level.toFixed(2)}</td>
                            <td>${new Date(item.timestamp * 1000).toLocaleString()}</td>
                        
                        
                        </tr>
                    `
                    tableBody.innerHTML += row
                })
                table.appendChild(tableBody)
                dataDisplay.appendChild(table)



            }
            else{
                dataDisplay.innerHTML = "Unexpected data format!"
                
            }


        }
        else{
            dataDisplay.innerHTML = "Failed to fetch data"
        }
    }
    catch(error){
        dataDisplay.innerHTML = "An error occured"
    }

}