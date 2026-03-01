import React, { useState } from "react";

function TopMenu() {
  return (
    <div className="w-full bg-black text-white px-4 py-3 flex items-center justify-between">
      <h1 className="text-lg font-bold m-0">       
         Impartial
      </h1>

    </div>
  );
}

function SectionNav({ active, setActive }) {
  const sections = ["Map", "Countries", "Events"];
  return (
    <div className="w-full flex flex-col">

      <div className="w-full h-px bg-white" />
      
      <div className="w-full flex">
        {sections.map((section) => (
          <button
            key={section}
            onClick={() => setActive(section)}
            className={`flex-1 py-2 text-center font-medium bg-transparent border-none outline-none cursor-pointer ${
              active === section
                ? "border-b-2 border-blue-500"
                : ""
            }`}
          >
            {section}
          </button>
        ))}
      </div>
    </div>
  );
}



function InfoPanel({ selectedEvent }) {
  if (!selectedEvent) {
    return (
      <div className="p-4">
      </div>
    );
  }

  return (
    <div className="p-4 space-y-2">
      <h2 className="text-xl font-semibold">{selectedEvent.title}</h2>
      <p className="text-gray-600">Year: {selectedEvent.year}</p>
      <p>{selectedEvent.description}</p>

   
    </div>
  );
}

function TimelineEvent({ event, onClick }) {
  return (
    <div
      onClick={() => onClick(event)}
      className="cursor-pointer border rounded-xl p-3 shadow hover:bg-gray-100"
    >
      <h4 className="font-semibold">{event.title}</h4>
    </div>
  );
}

function Timeline({ events, onSelect }) {
  return (
    <div className="h-full flex flex-col justify-center px-8">
      
      <div className="relative w-full h-2 bg-yellow-400 rounded">

        {events.map((event, index) => (
          <div
            key={event.id}
            className="absolute top-1/2 -translate-y-1/2"
            style={{ left: `${20 + index * 30}%` }}
          >
            <TimelineEvent event={event} onClick={onSelect} />
          </div>
        ))}

      </div>

    </div>
  );
}
export default function App() {
  const [activeSection, setActiveSection] = useState("Events");
  const [selectedEvent, setSelectedEvent] = useState(null);

  const events = [
    {
      id: 1,
      title: "World War II",
      year: 1939,
      description: "A global war lasting from 1939 to 1945.",
      children: [
        { id: 2, title: "Battle of Stalingrad" },
        { id: 3, title: "D-Day" },
      ],
    },
  ];

  return (
    <div className="h-screen flex flex-col">
      <TopMenu />

      <SectionNav active={activeSection} setActive={setActiveSection} />

      <div className="flex flex-1 overflow-hidden">

        <div className="w-1/2 border-r overflow-y-auto">
          <InfoPanel selectedEvent={selectedEvent} />
        </div>

          <div className="w-[5px] bg-white h-full"></div>

        <div className="w-1/2 overflow-y-auto">
          <Timeline events={events} onSelect={setSelectedEvent} />
        </div>
      </div>
      
    </div>

  );
}