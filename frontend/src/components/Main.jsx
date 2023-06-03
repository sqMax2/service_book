import AnonCarInfo from "./AnonCarInfo";
import {NavLink} from "react-router-dom";
import * as React  from "react";
import { Tab, Tabs, TabList, TabPanel } from 'react-tabs';
import 'react-tabs/style/react-tabs.css';
import withRouter from "./withRouter";

function Main(props) {
    const user = props.user


    return (
        <>
            <div>wtf?! Username: {user.username}, Full name: {user.first_name}. <b>Remove on prod!</b></div>
            {!user.username ?
                <AnonCarInfo /> :
                <>
                    <Tabs>
                        <TabList>
                          <Tab>Общая информация</Tab>
                          <Tab>Техническое обслуживание</Tab>
                          <Tab>Рекламации</Tab>
                          <Tab>Yoshi</Tab>
                          <Tab>Toad</Tab>
                        </TabList>

                        <TabPanel>
                        </TabPanel>
                    </Tabs>


                </>
            }
        </>
    )
}

export default withRouter(Main);