const NPKMBars = () => {
    const [levels, setLevels] = React.useState({
        N_level: 0,
        P_level: 0,
        K_level: 0,
        M_level: 0
    });

    const fetchData = async () => {
        try {
            const response = await fetch('http://127.0.0.1:5000/data');
            if (response.ok) {
                const data = await response.json();
                const latest_reading = data[data.length - 1];
                setLevels(latest_reading);
            }
        } catch(error) {
            console.error("Error fetching data: ", error);
        }
    };

    React.useEffect(() => {
        fetchData();
        const interval = setInterval(fetchData, 1000);
        return () => clearInterval(interval);
    }, []);

    const getNutrientStatus = (value) => {
        if (value < 10) return { text: "Very Low", color: "text-red-500" };
        if (value < 40) return { text: "Low", color: "text-yellow-500" };
        if (value < 70) return { text: "Optimal", color: "text-green-500" };
        if (value < 100) return { text: "High", color: "text-yellow-500" };
        return { text: "Very high", color: "text-red-500" };
    };

    const barColor = (level) => {
        if (level < 30) return 'bg-red-500';
        if (level < 70) return 'bg-yellow-500';
        return 'bg-green-500';
    };

    return (
        <div className="p-6 max-w-md mx-auto bg-white rounded-xl shadow-lg">
            <h2 className="text-xl font-bold mb-4">Live NPKM Levels</h2>
            
            {/* NPK Status Text */}
            <div className="mb-4">
                <div className="font-bold">
                    Nitrogen: {levels.N_level.toFixed(2)} mg/kg - 
                    <span className={getNutrientStatus(levels.N_level).color}>
                        {" "}{getNutrientStatus(levels.N_level).text}
                    </span>
                </div>
                <div className="font-bold">
                    Phosphorus: {levels.P_level.toFixed(2)} mg/kg - 
                    <span className={getNutrientStatus(levels.P_level).color}>
                        {" "}{getNutrientStatus(levels.P_level).text}
                    </span>
                </div>
                <div className="font-bold">
                    Potassium: {levels.K_level.toFixed(2)} mg/kg - 
                    <span className={getNutrientStatus(levels.K_level).color}>
                        {" "}{getNutrientStatus(levels.K_level).text}
                    </span>
                </div>
            </div>

            {/* Moisture Bar */}
            <div className="mb-6">
                <div className="flex items-center mb-1">
                    <span className="font-bold">Moisture: {levels.M_level.toFixed(2)}%</span>
                </div>
                <div className="w-full bg-gray-200 rounded-full h-4">
                    <div
                        className={`h-full rounded-full ${barColor(levels.M_level)} transition-all duration-500`}
                        style={{ width: `${Math.min(levels.M_level, 100)}%` }}
                    />
                </div>
            </div>
        </div>
    );
};

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<NPKMBars />);