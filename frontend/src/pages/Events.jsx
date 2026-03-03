import "./Events.css"
import { useState } from "react"
import PanelButton from "../components/PanelButton"

export default function Events(){
    const [panelState, changePanel] = useState(true)
    return (
        <div className="Event_view">
            

            <div className={panelState ? "Event_info": "Event_info hidden"}>

                <div className="Event_padding">
                    
                </div>
                    
                <div className="Event_name">
                    <h1> 
                        Dien Bien Phu
                    </h1>
                </div>

            <div className={panelState ? "Event_button" : "Event_button hidden"}>
                <PanelButton panelState={panelState} changePanel = {changePanel}/>
            </div>
           
                <div className="Event_date">
                    13 March to 7 May 1954 
                </div>


                <div className="Event_padding"></div>

                <div className="Event_summary"> 
                    <br></br>
                    <h3> Summary </h3> 
                </div>
                
                <div className="Event_summary_spacing"></div>


                <div className="Event_themes">
                    themes
                </div>

          </div>

            <div className="vline"></div>


            <div className={panelState ? "Event_timeline": "Event_timeline expanded"}>

                <div className= "Timeline_w_stamps">
                    <div className="Timestamps">
                        <div className="stuff"> start </div>
                        <div className="stuff"> end </div>
                    </div>

                    <div className="Timeline"></div>
                </div>

                
            </div>
        </div>

    )
}

