# Chemical Formula Finder App
# Author: Claude
# Description: A Streamlit application that uses PubChemPy to look up 
# chemical formulas and related information based on chemical names.

import streamlit as st
import pubchempy as pcp
import time

def main():
    """
    Main function that sets up the Streamlit application interface.
    """
    # Set up the page with a title and description
    st.set_page_config(page_title="Chemical Formula Finder", page_icon="🧪")
    st.title("Chemical Formula Finder")
    st.markdown("""
    This app lets you search for chemical information using PubChemPy.
    Enter a chemical name to find its formula, IUPAC name, and other details.
    """)
    
    # Sidebar with information about the app
    with st.sidebar:
        st.header("About")
        st.info("""
        This app uses the PubChemPy library to retrieve chemical information 
        from the PubChem database maintained by the National Institutes of Health.
        """)
        st.markdown("### Installation")
        st.code("pip install pubchempy streamlit")
        
    # Create the input field for the chemical name
    chemical_name = st.text_input("Enter chemical name:", placeholder="e.g., Methane, Aspirin, Caffeine")
    
    # Add a search button
    search_button = st.button("Search")
    
    # Only search when the user has entered a name and clicked the button
    if chemical_name and search_button:
        with st.spinner(f"Searching for {chemical_name}..."):
            search_chemical(chemical_name)

def search_chemical(chemical_name):
    """
    Search for a chemical compound by name and display its information.
    
    Args:
        chemical_name (str): The name of the chemical to search for
    """
    try:
        # Attempt to retrieve compound information from PubChem
        # The get_compounds function returns a list of matching compounds
        # We take the first result [0] as it's typically the most relevant
        compound = pcp.get_compounds(chemical_name, 'name')[0]
        
        # Display the chemical information in a clean format
        st.subheader("Chemical Information")
        
        # Create two columns for better layout
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"**IUPAC Name:** {compound.iupac_name}")
            
            # Get synonyms/common names (if available)
            if hasattr(compound, 'synonyms') and compound.synonyms:
                st.markdown(f"**Common Name:** {compound.synonyms[0]}")
            else:
                st.markdown("**Common Name:** Not available")
            
            st.markdown(f"**Molecular Weight:** {compound.molecular_weight}")
            st.markdown(f"**Formula:** {compound.molecular_formula}")
        
        with col2:
            # Display additional information if available
            if hasattr(compound, 'cid'):
                st.markdown(f"**PubChem CID:** {compound.cid}")
                
                # Display the compound image from PubChem
                image_url = f"https://pubchem.ncbi.nlm.nih.gov/image/imgsrv.fcgi?cid={compound.cid}&t=l"
                st.image(image_url, caption=f"Structure of {chemical_name}")
        
        # Display more detailed information in an expandable section
        with st.expander("More Details"):
            # Convert compound to dictionary for display
            compound_dict = compound.to_dict()
            # Remove potentially large entries that might clutter the display
            for key in ['atoms', 'bonds', 'elements', 'coordinates']:
                if key in compound_dict:
                    compound_dict[key] = f"[{len(compound_dict[key])} entries]"
            
            st.json(compound_dict)
            
            # Add a link to PubChem for more information
            st.markdown(f"[View on PubChem](https://pubchem.ncbi.nlm.nih.gov/compound/{compound.cid})")
    
    except IndexError:
        # Handle the case where no compounds were found
        st.error(f"No information found for '{chemical_name}'.")
        st.markdown("""
        **Possible reasons:**
        - The chemical name may be misspelled
        - The compound may not be in the PubChem database
        - Try using a more common name or the IUPAC name
        """)
    
    except Exception as e:
        # Handle any other exceptions that might occur
        st.error(f"An error occurred: {str(e)}")
        st.markdown("Please try again or search for a different chemical.")

# Run the app
if __name__ == "__main__":
    main()
