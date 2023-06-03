import AnonCarInfo from "./AnonCarInfo";
import {NavLink} from "react-router-dom";
import * as React  from "react";
import withRouter from "./withRouter";

function Main(props) {
    // const [user, setUser] = React.useState({});
    // const updateUser = (user_data) => {
    //     console.log('--user updated--');
    //     // setUser(user_data);
    // }
    const user = props.user
    console.log(user)
    return (
        <>
            <div>wtf?! Username: {user.username}, Full name: {user.first_name}. <b>Remove on prod!</b></div>
            {!user.username ?
                <>
                    <AnonCarInfo />
                </> :
                <>

                </>
            }
        </>
    )
}

export default withRouter(Main);