/**
 * Copyright 2024 Google LLC
 * 
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 * 
 *    https://www.apache.org/licenses/LICENSE-2.0
 * 
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
*/

import React from 'react';
import { createRoot } from "react-dom/client";
import { APIProvider, Map } from '@vis.gl/react-google-maps';

const App = () => {
  const [narrativeContent, setNarrativeContent] = React.useState('');

  React.useEffect(() => {
    const fetchNarrativeContent = async () => {
      try {
        const response = await fetch('http://localhost:5000/narrative-content');
        if (!response.ok) {
          throw new Error('Failed to fetch narrative content');
        }
        const data = await response.text();
        setNarrativeContent(data);
      } catch (error) {
        console.error('Error fetching narrative content:', error);
        setNarrativeContent('Failed to load narrative content.');
      }
    };
    fetchNarrativeContent();
  }, []);

  return (
    <div style={{ height: '100vh', width: '100vw' }}>
      <APIProvider apiKey={import.meta.env.VITE_GOOGLE_MAPS_API_KEY} onLoad={() => console.log('Maps API has loaded.')}>
        <Map
          defaultZoom={13}
          defaultCenter={{ lat: 40.7128, lng: -74.0060 }}
          mapId='DEMO_MAP_ID'
        >
          {/* You can add markers or other map components here */}
        </Map>
      </APIProvider>
      <div style={{ position: 'absolute', top: '10px', left: '10px', backgroundColor: 'white', padding: '10px', borderRadius: '5px' }}>
        <h1>Narrative Content</h1>
        <p>{narrativeContent}</p>
      </div>
    </div>
  );
};

const appElement = document.getElementById('app');
if (appElement) {
  const root = createRoot(appElement);
  root.render(<App />);
} else {
  console.error('Failed to find the app element');
}

export default App;