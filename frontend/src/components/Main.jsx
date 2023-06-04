import AnonCarInfo from "./AnonCarInfo";
import {NavLink} from "react-router-dom";
import * as React  from "react";
import { Tab, Tabs, TabList, TabPanel } from 'react-tabs';
import 'react-tabs/style/react-tabs.css';
import withRouter from "./withRouter";
import axios from "axios";
import {Table} from "react-bootstrap";

function Main(props) {
    const [library, setLibrary] = React.useState({});
    const [carData, setCarData] = React.useState([]);
    const [maintenanceData, setMaintenanceData] = React.useState([]);
    const [reclamationData, setReclamationData] = React.useState([]);
    const user = props.user

    const objectMap = (obj, fn) => Object.entries(obj).map(([k, v], i) => fn(v, k, i)
    )

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

    const expandElement = (e) => {
        console.log(e.target.closest('tr').dataset.id)
        console.log(e.target.closest('tbody').className)
    }

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
                          <Tab disabled>Подробности</Tab>
                          <Tab disabled>Каталоги</Tab>
                        </TabList>

                        <TabPanel>
                            <div className={'table-sorting'}></div>
                            <div className={'table'}>
                                <table className={"table-striped"}>
                                    <thead>
                                        <tr>
                                            {library.car ? objectMap(library.car, val => {
                                                return (
                                                    <th>{val}</th>
                                                )}):''}
                                        </tr>
                                    </thead>
                                    <tbody className={"car-data"}>
                                    {carData.map(elem => dataMap(elem))}
                                    </tbody>
                                </table>
                            </div>
                        </TabPanel>
                        <TabPanel>
                            <div className={'table-sorting'}></div>
                            <div className={'table'}>
                                <table className={"table-striped"}>
                                    <thead>
                                        <tr>
                                            {library.maintenance ? objectMap(library.maintenance, val => {
                                                return (<th>{val}</th>) }):''}
                                        </tr>
                                    </thead>
                                    <tbody className={"maintenance-data"}>
                                    {maintenanceData.map(elem => dataMap(elem))}
                                    </tbody>
                                </table>
                            </div>
                        </TabPanel>
                        <TabPanel>
                            <div className={'table-sorting'}></div>
                            <div className={'table'}>
                                <table className={"table-striped"}>
                                    <thead>
                                        <tr>
                                            {library.reclamation ? objectMap(library.reclamation, val => {
                                                return (
                                                    <th>{val}</th>
                                                )}):''}
                                        </tr>
                                    </thead>
                                    <tbody className={"reclamation-data"}>
                                    {reclamationData.map(elem => dataMap(elem))}
                                    </tbody>
                                </table>
                            </div>
                        </TabPanel>
                        <TabPanel>
                        </TabPanel>
                        <TabPanel>
                        </TabPanel>
                    </Tabs>


                </>
            }
        </>
    )
}

export default withRouter(Main);