# car-rental-system

### Non-Terminal Symbols ($V$)

$$
\begin{align*}
V =
\{ \,
& \text{cars}, \text{car\_list}, \text{car}, \text{services}, \text{service\_list}, \text{service}, \\
& \text{id}, \text{brand}, \text{model}, \text{year}, \text{license\_plate}, \text{available}, \\
& \text{rental\_price}, \text{transmission}, \text{date}, \text{description}, \\
& \text{car\_id}, \text{car\_brand}, \text{car\_model}, \text{car\_year}, \text{car\_license\_plate}
\, \}
\end{align*}
$$

### Terminal Symbols ($T$)

The set of terminal symbols is given by:

$$
\begin{align*}
T = \{\, &
\text{ID}, \text{TEXT}, \text{YEAR}, \text{LICENSE\_PLATE}, \text{AVAILABLE}, \text{RENTAL\_PRICE}, \text{TRANSMISSION}, \text{DATE}, \\
& \text{CARS\_O}, \text{CARS\_C}, \text{CAR\_O}, \text{CAR\_C}, \text{ID\_O}, \text{ID\_C}, \text{BRAND\_O}, \text{BRAND\_C}, \\
& \text{MODEL\_O}, \text{MODEL\_C}, \text{YEAR\_O}, \text{YEAR\_C}, \text{LICENSE\_PLATE\_O}, \text{LICENSE\_PLATE\_C}, \\
& \text{AVAILABLE\_O}, \text{AVAILABLE\_C}, \text{RENTAL\_PRICE\_O}, \text{RENTAL\_PRICE\_C}, \\
& \text{TRANSMISSION\_O}, \text{TRANSMISSION\_C}, \text{SERVICES\_O}, \text{SERVICES\_C}, \\
& \text{SERVICE\_O}, \text{SERVICE\_C}, \text{DATE\_O}, \text{DATE\_C}, \text{DESCRIPTION\_O}, \text{DESCRIPTION\_C}
\,\}
\end{align*}
$$

#### Tokens

- CARS_O: `<cars>`
- CARS_C: `</cars>`
- CAR_O: `<car>`
- CAR_C: `</car>`
- ID_O: `<id>`
- ID_C: `</id>`
- BRAND_O: `<brand>`
- BRAND_C: `</brand>`
- MODEL_O: `<model>`
- MODEL_C: `</model>`
- YEAR_O: `<year>`
- YEAR_C: `</year>`
- LICENSE_PLATE_O: `<license_plate>`
- LICENSE_PLATE_C: `</license_plate>`
- AVAILABLE_O: `<available>`
- AVAILABLE_C: `</available>`
- RENTAL_PRICE_O: `<rental_price>`
- RENTAL_PRICE_C: `</rental_price>`
- TRANSMISSION_O: `<transmission>`
- TRANSMISSION_C: `</transmission>`
- SERVICES_O: `<services>`
- SERVICES_C: `</services>`
- SERVICE_O: `<service>`
- SERVICE_C: `</service>`
- DATE_O: `<date>`
- DATE_C: `</date>`
- DESCRIPTION_O: `<description>`
- DESCRIPTION_C: `</description>`
- LICENSE_PLATE: `[A-Z]{3}-[0-9]{3}`
- YEAR: `[0-9]{4}`
- ID: `[0-9]{3}`
- AVAILABLE: `(?:true|false)`
- RENTAL_PRICE: `[0-9]+\.[0-9]{2}`
- TRANSMISSION: `(?:automatic|manual)`
- DATE: `[0-9]{4}-(?:0[1-9]|[1][0-1])-(?:0[1-9]|1[0-9]|2[0-9]|3[0-1])`
- TEXT: `[^<]+`

### Production Rules ($P$)

- `cars → CARS_O car_list CARS_C`
- `car_list → car car_list + ε`
- `car → CAR_O id brand model year license_plate available rental_price transmission services CAR_C`
- `id → ID_O ID ID_C`
- `brand → BRAND_O TEXT BRAND_C`
- `model → MODEL_O TEXT MODEL_C`
- `year → YEAR_O YEAR YEAR_C`
- `license_plate → LICENSE_PLATE_O LICENSE_PLATE LICENSE_PLATE_C`
- `available → AVAILABLE_O AVAILABLE AVAILABLE_C`
- `rental_price → RENTAL_PRICE_O RENTAL_PRICE RENTAL_PRICE_C`
- `transmission → TRANSMISSION_O TRANSMISSION TRANSMISSION_C`
- `services → SERVICES_O service_list SERVICES_C`
- `service_list → service service_list + ε`
- `service → SERVICE_O date description SERVICE_C`
- `date → DATE_O DATE DATE_C`
- `description → DESCRIPTION_O TEXT DESCRIPTION_C`

### Initial State ($S$)

$$
S = \text{cars}
$$
