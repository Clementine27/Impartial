import "./Events.css"
import { useState } from "react"
import PanelButton from "../components/PanelButton"
import { useLoaderData } from "react-router-dom";

export default function Events() {
    const data = useLoaderData()
    if (!data){
        // TODO: custom error handler 
        console.log("fetching data failed")
    }

    // TODO: if endDate and startDate same year, then display once 
    const startDate = new Date(data.start).toLocaleDateString("en-US", { year: "numeric", month: "long", day: "numeric" })
    const endDate = new Date(data.end).toLocaleDateString("en-US", { year: "numeric", month: "long", day: "numeric" })

    const [panelState, changePanel] = useState(true)
    return (
        <div className="Event_view">


            <div className={panelState ? "Event_info" : "Event_info hidden"}>

                <div className="Event_padding"></div>

                <div className="Event_name">
                    <h1>
                        {data.name}
                    </h1>
                </div>

                <div className={panelState ? "Event_button" : "Event_button hidden"}>
                    <PanelButton panelState={panelState} changePanel={changePanel} />
                </div>

                <div className="Event_date">
                    { startDate == endDate ? startDate : `${startDate}  to ${endDate}`}
                </div>

                <div className="Event_padding"></div>

                {/*TODO: insert link */}
                <div className="Event_summary">
                    <br></br>
                    <h3> 
                        {data.summary ? data.summary : "welp"} </h3>
                </div>

                <div className="Event_summary_spacing"></div>


                <div className="Event_themes">
                    {data.themes ? data.themes : "lol"}

                </div>

            </div>

            <div className="vline"></div>


            <div className={panelState ? "Event_timeline" : "Event_timeline expanded"}>

                <div className="Timeline_w_stamps">
                    <div className="Timestamps">
                        <div className="stuff"> {startDate} </div>
                        <div className="stuff"> {endDate} </div>
                    </div>

                    <div className="Timeline"></div>
                </div>


            </div>
        </div>

    )
}

