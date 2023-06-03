import * as React  from "react";
import {Button, Table} from "react-bootstrap";
import axios from "axios";

function AnonCarInfo () {

    const searchRequest = (e) => {
        const searchNumber = document.getElementById("car-number").value;
        const searchResult = document.getElementsByClassName("search-result")[0];
        const carDataRow = document.getElementsByClassName("car-data-row")[0];

        axios.get('/api/car/' + searchNumber + "/")
        .then(res => {
            const car = res.data;
            const field_list = car.field_list;
            searchResult.innerHTML = 'Информация о комплектации и технических характеристиках Вашей техники';
            let table = '';
            for (let field in field_list) {
                let value = eval("car."+field);
                if (value.slice(0,4) === "http") {
                    value = eval("car."+field+"Name");
                }
                table += `<td data-cell="${field_list[field]}">${value}</td>`
            }
            carDataRow.innerHTML = table;
            // carDataRow.innerHTML = `<td>${car.carNumber}</td>
            //                     <td>${car.techniqueModelName}</td>
            //                     <td>${car.engineModelName}</td>
            //                     <td>${car.engineNumber}</td>
            //                     <td>${car.transmissionModelName}</td>
            //                     <td>${car.transmissionNumber}</td>
            //                     <td>${car.driveAxleModelName}</td>
            //                     <td>${car.driveAxleNumber}</td>
            //                     <td>${car.steerableAxleModelName}</td>
            //                     <td>${car.steerableAxleNumber}</td>`
            // console.log('user: ', user)
        })
        .catch((e) => {
            searchResult.innerHTML = 'Машина не найдена';
        })
    }

    return (
        <>
            <div className={"car-search"}>
                <p>Проверьте комплектацию и технические характеристики техники Силант</p>
                <label htmlFor={"car-number"}>Заводской номер машины</label>
                <input id={"car-number"} placeholder={"Номер машины"}
                       onKeyDown={(evt) => {if (evt.keyCode === 13) searchRequest(evt)}}
                       onsize={20} maxLength={64}/>
                <Button id={"car-number-submit"} onClick={searchRequest}>Найти</Button>
            </div>
            <div className={"car-search-result"}>
                <p>Результат поиска:</p>
                <p className={"search-result"}></p>
                <Table striped responsive={"lg"}>
                    <thead>
                        <tr>
                            <th>Заводской номер машины</th>
                            <th>Модель техники</th>
                            <th>Модель двигателя</th>
                            <th>Заводской номер двигателя</th>
                            <th>Модель трансмиссии</th>
                            <th>Заводской номер трансмиссии</th>
                            <th>Модель ведущего моста</th>
                            <th>Заводской номер ведущего моста</th>
                            <th>Модель управляемого моста</th>
                            <th>Заводской номер управляемого моста</th>
                        </tr>
                    </thead>
                    <tbody>
                    <tr className={"car-data-row"}>

                    </tr>
                    </tbody>
                </Table>
            </div>
        </>
    )
}

export default AnonCarInfo;