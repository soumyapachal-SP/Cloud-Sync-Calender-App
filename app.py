# -*- coding: utf-8 -*-
"""Cloud_Proj.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Cr27BbgoOXl8fVBln3QcJbiH7lH8sotx
"""

pip install gradio

import gradio as gr
import datetime

# Sample events list to store added events
events = []

def add_event(title, date, description):
    try:
        # Validate date
        event_date = datetime.datetime.strptime(date, "%Y-%m-%d")
        events.append({"title": title, "date": event_date, "description": description})
        return f"Event '{title}' added successfully!"
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

def display_events():
    if not events:
        return "No events available."
    return "\n".join([f"{e['title']} - {e['date'].strftime('%Y-%m-%d')}\nDescription: {e['description']}" for e in events])

# Gradio Interface
with gr.Blocks() as app:
    gr.Markdown("## Add Event")
    title_input = gr.Textbox(label="Event Title")
    date_input = gr.Textbox(label="Event Date (YYYY-MM-DD)")
    desc_input = gr.Textbox(label="Event Description")
    submit_button = gr.Button("Add Event")
    result_output = gr.Textbox(label="Result")

    gr.Markdown("## Event List")
    event_output = gr.Textbox(label="Events", interactive=False)

    submit_button.click(add_event, inputs=[title_input, date_input, desc_input], outputs=[result_output])
    submit_button.click(display_events, outputs=[event_output])

app.launch()

