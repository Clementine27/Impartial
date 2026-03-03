
import { GoTriangleRight} from "react-icons/go";
import "./PanelButton.css"
export default function PanelButton({panelState, changePanel}){
    return (
         <button
         className= {panelState ? "clicked": "unclicked"}
            onClick={() => changePanel(!panelState)}>
                <GoTriangleRight />
            </button>
    )
}
