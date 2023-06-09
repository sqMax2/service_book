import AnonCarInfo from "./AnonCarInfo";
import {NavLink} from "react-router-dom";
import * as React  from "react";
import { Tab, Tabs, TabList, TabPanel } from 'react-tabs';
import 'react-tabs/style/react-tabs.css';
import withRouter from "./withRouter";
import axios from "axios";
import {Table} from "react-bootstrap";
import {forEach} from "react-bootstrap/ElementChildren";

function Main(props) {
    const [library, setLibrary] = React.useState({});
    const [carData, setCarData] = React.useState([]);
    const [maintenanceData, setMaintenanceData] = React.useState([]);
    const [reclamationData, setReclamationData] = React.useState([]);
    const [detailObject, setDetailObject] = React.useState([]);
    const user = props.user

    const objectMap = (obj, fn) => Object.entries(obj).map(([k, v], i) => fn(v, k, i)
    )
    const tableSort = (table, column, ascend) => {
        let sortedRows = Array.from(table.rows)
        .slice(1)
        .sort((rowA, rowB) => rowA.cells[column].innerHTML > rowB.cells[column].innerHTML ? -1 + 2 * ascend : 1 - 2 * ascend);
        table.tBodies[0].append(...sortedRows);
    }

    const get_library = () => {
        axios.get('/api/library/')
        .then(res => {
            const lib = res.data;
            setLibrary(lib);
        })
    }

    const dataMap = (obj) => {

        let elems = [];
        let field_list = obj.field_list;
        let id = obj.carNumber ? obj.carNumber : null ;
        for (let field in field_list) {
            let value = eval("obj."+field);
            if (field === 'id') {
                id = value;
                continue;
            }
            if (value && (value.length > 4)) {
                if (value.slice(0,4) === "http") {
                    value = eval("obj."+field+"Name");
                }
            }
            if (field === "car") {
                value = eval("obj."+field+"Number");
            }
            elems.push(<td data-cell={field_list[field]}>{value}</td>);
        }
        let result = <tr onClick={expandElement} data-id={id}>{elems}</tr>

        return (result);
    }

    const get_data = () => {
        // let carData = document.getElementsByClassName("car-data")[0];
        axios.get('/api/car/')
        .then(res => {
            const cars = res.data.results;
            setCarData(cars);
        });
        if (props.user.username) {
            axios.get('/api/maintenance/')
            .then(res => {
                const maintenances = res.data.results;
                setMaintenanceData(maintenances);
            });
            axios.get('/api/reclamation/')
            .then(res => {
                const reclamations = res.data.results;
                setReclamationData(reclamations);
            });
        }
    }

    const sortHandler = (e) => {
        let header = e.target;
        let index = header.cellIndex;
        let table = header.closest('table');
        let sign = document.createElement('div');
        let prev_sorted = table.querySelectorAll('.asc,.desc');
        prev_sorted.forEach((elem) => {
            if (elem !== header) {
                elem.classList.remove('asc', 'desc');
            }
        })
        if (header.classList.contains('asc')) {
            header.classList.add('desc');
            header.classList.remove('asc');
            tableSort(table, index, false);
        }
        else {
            header.classList.add('asc');
            header.classList.remove('desc');
            tableSort(table, index, true);
        }

    }

    const expandElement = (e) => {
        console.log(e.target.closest('tr').dataset.id)
        console.log(e.target.closest('tbody').className)
        let tab_detail = document.getElementById("tab:r0:3");
        let tab_panel_detail = document.getElementById("panel:r0:3");

        tab_detail.click();

        let detail_info = [];
        let object = {};
        let lib = {};

        switch (e.target.closest('tbody').className) {
            case 'car-data':
                object = carData.find(element => element.carNumber === e.target.closest('tr').dataset.id);
                lib = library.car;
                break;
            case 'maintenance-data':
                object = maintenanceData.find(element => Number(element.id) === Number(e.target.closest('tr').dataset.id));
                lib = library.maintenance;
                break;
            case 'reclamation-data':
                object = reclamationData.find(element => Number(element.id) === Number(e.target.closest('tr').dataset.id));
                lib = library.reclamation;
        }
        for (let field in lib) {
            let value = object[field];
            if (field === 'id') {
                continue;
            }
            if (value && (value.length > 4)) {
                if (value.slice(0,4) === "http") {
                    value = object[field+"Name"];
                }
            }
            if (field === "car") {
                value = object[field+"Number"];
            }
            detail_info.push(<div>{lib[field]}: {value}</div>);
        }
        setDetailObject(detail_info);
    };

    React.useEffect(() => {get_library();}, []);
    React.useEffect(() => get_data(), [props.user])

    return (
        <>
            {!user.username ?
                <AnonCarInfo /> :
                <>
                    <Tabs>
                        <TabList>
                          <Tab>Общая информация</Tab>
                          <Tab>Техническое обслуживание</Tab>
                          <Tab>Рекламации</Tab>
                          <Tab>Подробности</Tab>
                          <Tab disabled>Каталоги</Tab>
                        </TabList>

                        <TabPanel className={"tab-panel-car"}>
                            <div className={'table-sorting'}></div>
                            <div className={'table'}>
                                <table className={"table-striped"}>
                                    <thead>
                                        <tr>
                                            {library.car ? objectMap(library.car, val => {
                                                return (
                                                    <th onClick={sortHandler}>{val}</th>
                                                )}):''}
                                        </tr>
                                    </thead>
                                    <tbody className={"car-data"}>
                                    {carData.map(elem => dataMap(elem))}
                                    </tbody>
                                </table>
                            </div>
                        </TabPanel>
                        <TabPanel className={"tab-panel-maintenance"}>
                            <div className={'table-sorting'}></div>
                            <div className={'table'}>
                                <table className={"table-striped"}>
                                    <thead>
                                        <tr>
                                            {library.maintenance ? objectMap(library.maintenance, val => {
                                                return (<th onClick={sortHandler}>{val}</th>) }):''}
                                        </tr>
                                    </thead>
                                    <tbody className={"maintenance-data"}>
                                    {maintenanceData.map(elem => dataMap(elem))}
                                    </tbody>
                                </table>
                            </div>
                        </TabPanel>
                        <TabPanel className={"tab-panel-reclamation"}>
                            <div className={'table-sorting'}></div>
                            <div className={'table'}>
                                <table className={"table-striped"}>
                                    <thead>
                                        <tr>
                                            {library.reclamation ? objectMap(library.reclamation, val => {
                                                return (
                                                    <th onClick={sortHandler}>{val}</th>
                                                )}):''}
                                        </tr>
                                    </thead>
                                    <tbody className={"reclamation-data"}>
                                    {reclamationData.map(elem => dataMap(elem))}
                                    </tbody>
                                </table>
                            </div>
                        </TabPanel>
                        <TabPanel className={"tab-panel-detail"}>
                            <div className={'detail'}>
                                {detailObject ? detailObject : ''}
                            </div>
                        </TabPanel>
                        <TabPanel className={"tab-panel-catalogue"}>
                        </TabPanel>
                    </Tabs>


                </>
            }
        </>
    )
}

export default withRouter(Main);