# Rent Match
An application designed for Hack for Homes 2025.
**Problem:** Tenants, even those with valid documentation, are forced to mass apply and get rejected repeatedly, creating an unnecessary backlog. Similarly, landlords receive overwhelming amounts of applications and cannot afford to assess them fairly.

Our application aims to address these issues by:
**Eliminating mass applications for both landlords and tenants:** Efficiently match tenants and landlords based off preferences with a Tinder-based swiping system and an AI-rental recommendation system.
**Reduce bias:** Tenants will verify valid documentation which landlords can view, decreasing the chances of them being blindly rejected.
**Builds trust:** A chat feature directly connects matched tenants and landlords, speeding up the process of securing a rental.

---
## Table of Contents
- [Setup Instructions](#setup-instructions)
- [Team Members](#team-members)


## Setup Instructions

1. **Open the repository**
   Open the project directory in your terminal.

2. **Create a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt

   ```
4. **Create A Folder for the Database**
   ```bash
   mkdir instance
   ```

5. **Run the app**

```bash
+ flask db upgrade  # Run database migrations (if using Flask-Migrate)
+ flask run

```

## Team Members

<table>
  <tr>
    <th>Name</th>
    <th>GitHub Username</th>
  </tr>
  <tr>
    <td>Punit Nitin Patil</td>
    <td>Punit750</td>
  </tr>
  <tr>
    <td>Caroline Ann</td>
    <td>CrimsonW23</td>
  </tr>
  <tr>
    <td>Lim Zhen Yi</td>
    <td>l-zhenyi</td>
  </tr>
  <tr>
    <td>Dharun Somalingam</td>
    <td>DharunSomalingam</td>
  </tr>
    <tr>
       <td>Pranit Kasturi</td>
       <td>Pranit-Kasturi</td>
  </tr>
</table>
