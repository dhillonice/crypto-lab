#include <stdio.h>
#include <string.h>

#define MAX_WAYPOINTS 10

// ==========================================
// WAYPOINT STRUCTURE
// ==========================================

struct Waypoint {
    float latitude;
    float longitude;
    float altitude;

    // Vulnerability #2:
    // Small buffer used without input length validation.
    char name[20];
};


// ==========================================
// TELEMETRY STRUCTURE
// ==========================================

struct Telemetry {
    float latitude;
    float longitude;
    float altitude;
    int battery;
    char status[20];
};


// ==========================================
// FUNCTION DECLARATIONS
// ==========================================

void login();

void uploadWaypoints(
    struct Waypoint waypoints[],
    int *count
);

void executeMission(
    struct Waypoint waypoints[],
    int count,
    struct Telemetry *telemetry
);

void displayTelemetry(
    struct Telemetry *telemetry
);

void saveLogs(
    struct Waypoint waypoints[],
    int count
);


// ==========================================
// MAIN
// ==========================================

int main() {

    struct Waypoint waypoints[MAX_WAYPOINTS];

    int waypointCount = 0;

    struct Telemetry telemetry = {
        0.0,
        0.0,
        0.0,
        100,
        "STANDBY"
    };


    printf("=====================================\n");
    printf("       DRONE CONTROL SYSTEM\n");
    printf("=====================================\n");


    // ======================================
    // 1. LOGIN
    // ======================================

    printf("\n========== LOGIN ==========\n");

    /*
       VULNERABILITY #1:
       Missing Authentication

       Username and password are collected,
       but they are NOT verified.
    */

    login();

    printf("\nLogin successful!\n");
    printf("Proceeding to drone operations...\n");


    // ======================================
    // 2. WAYPOINT UPLOAD
    // ======================================

    uploadWaypoints(
        waypoints,
        &waypointCount
    );


    if (waypointCount == 0) {

        printf("\nNo waypoints uploaded.\n");
        printf("Mission cannot be executed.\n");

        return 0;
    }


    // ======================================
    // 3. MISSION EXECUTION
    // ======================================

    executeMission(
        waypoints,
        waypointCount,
        &telemetry
    );


    // ======================================
    // 4. LOG STORAGE
    // ======================================

    saveLogs(
        waypoints,
        waypointCount
    );


    printf("\n=====================================\n");
    printf("       DRONE MISSION COMPLETED\n");
    printf("=====================================\n");

    return 0;
}


// ==========================================
// LOGIN
// ==========================================

void login() {

    char username[50];
    char password[50];


    printf("Enter username: ");
    scanf("%49s", username);

    printf("Enter password: ");
    scanf("%49s", password);


    /*
       VULNERABILITY #1:
       Missing Authentication

       The username and password are accepted,
       but no verification is performed.

       Any username/password combination is
       allowed to continue.
    */
}


// ==========================================
// WAYPOINT UPLOAD
// ==========================================

void uploadWaypoints(
    struct Waypoint waypoints[],
    int *count
) {

    int number;


    printf("\n====== WAYPOINT UPLOAD ======\n");


    printf(
        "Enter number of waypoints (1-%d): ",
        MAX_WAYPOINTS
    );

    scanf("%d", &number);


    if (
        number < 1 ||
        number > MAX_WAYPOINTS
    ) {

        printf("Invalid number of waypoints!\n");

        *count = 0;

        return;
    }


    for (int i = 0; i < number; i++) {

        printf("\nWaypoint %d\n", i + 1);


        // ==================================
        // VULNERABILITY #2:
        // BUFFER OVERFLOW
        // ==================================

        printf("Enter waypoint name: ");

        /*
           VULNERABLE:
           No maximum length is specified.

           waypointName buffer has only 20 bytes,
           but scanf can read an arbitrarily long
           string.
        */

        scanf(
            "%s",
            waypoints[i].name
        );


        printf("Enter latitude: ");

        scanf(
            "%f",
            &waypoints[i].latitude
        );


        printf("Enter longitude: ");

        scanf(
            "%f",
            &waypoints[i].longitude
        );


        printf("Enter altitude: ");

        scanf(
            "%f",
            &waypoints[i].altitude
        );
    }


    *count = number;


    printf(
        "\n%d waypoint(s) uploaded successfully!\n",
        number
    );
}


// ==========================================
// MISSION EXECUTION
// ==========================================

void executeMission(
    struct Waypoint waypoints[],
    int count,
    struct Telemetry *telemetry
) {

    printf("\n====== MISSION EXECUTION ======\n");

    printf("Starting drone mission...\n");


    for (int i = 0; i < count; i++) {

        printf(
            "\nMoving to Waypoint %d...\n",
            i + 1
        );


        printf(
            "Waypoint Name: %s\n",
            waypoints[i].name
        );


        // ==================================
        // UPDATE TELEMETRY
        // ==================================

        telemetry->latitude =
            waypoints[i].latitude;

        telemetry->longitude =
            waypoints[i].longitude;

        telemetry->altitude =
            waypoints[i].altitude;


        // Simulated battery consumption
        telemetry->battery =
            100 - ((i + 1) * 5);


        strcpy(
            telemetry->status,
            "ACTIVE"
        );


        displayTelemetry(telemetry);


        printf(
            "Reached Waypoint %d.\n",
            i + 1
        );
    }


    strcpy(
        telemetry->status,
        "COMPLETED"
    );


    printf(
        "\nMission completed successfully!\n"
    );

    printf(
        "Final Status: %s\n",
        telemetry->status
    );
}


// ==========================================
// TELEMETRY
// ==========================================

void displayTelemetry(
    struct Telemetry *telemetry
) {

    printf("\n------ CURRENT TELEMETRY ------\n");


    printf(
        "Latitude : %.4f\n",
        telemetry->latitude
    );


    printf(
        "Longitude: %.4f\n",
        telemetry->longitude
    );


    printf(
        "Altitude : %.2f m\n",
        telemetry->altitude
    );


    printf(
        "Battery  : %d %%\n",
        telemetry->battery
    );


    printf(
        "Status   : %s\n",
        telemetry->status
    );


    printf(
        "-------------------------------\n"
    );
}


// ==========================================
// LOG STORAGE
// ==========================================

void saveLogs(
    struct Waypoint waypoints[],
    int count
) {

    char filename[100];

    FILE *file;


    printf("\n====== LOG STORAGE ======\n");


    printf(
        "Enter log filename: "
    );


    // ======================================
    // VULNERABILITY #3:
    // INSECURE FILE HANDLING
    // ======================================

    /*
       User controls the filename/path and
       the program does not validate it.
    */

    scanf(
        "%99s",
        filename
    );


    /*
       VULNERABLE:
       User-controlled filename is directly
       passed to fopen().
    */

    file = fopen(
        filename,
        "a"
    );


    if (file == NULL) {

        printf(
            "\nError: Could not open log file.\n"
        );

        return;
    }


    fprintf(
        file,
        "\n========== NEW MISSION ==========\n"
    );


    for (int i = 0; i < count; i++) {

        fprintf(
            file,
            "Waypoint %d: "
            "Name=%s, "
            "Latitude=%.4f, "
            "Longitude=%.4f, "
            "Altitude=%.2f\n",

            i + 1,

            waypoints[i].name,

            waypoints[i].latitude,

            waypoints[i].longitude,

            waypoints[i].altitude
        );
    }


    fprintf(
        file,
        "Mission Status: COMPLETED\n"
    );


    fclose(file);


    printf(
        "Mission log saved successfully.\n"
    );
}