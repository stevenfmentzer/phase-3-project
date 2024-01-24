# Phase 3 Project

Creators: Steven Mentzer, Igor Rakush, Tyler Kim

## App Description
An interface to quickly design and schedule art exhibitions and track an artworks location.

## Model Classes
- Owner
- Art 
- Museum
- Exhibition
- Request

## Domain Model Table
View draw.io file

## CRUD rough idea
- Create: 
    - User objects as 'Museum' or 'Owner'
    - 'Museum's can create new 'Exhibition's
- Read: 
    - 'Musuem' and 'Owner' can access data on exhibtions and art objects 
- Update: 
    - 'Musuem' and 'Owner' change dates on exhibtions
    - 'Owner' can change the art value
- Delete: 
    - Delete an artwork

## Museum User Functionality:

### Museum Class Functions
- get_all_museum()
- create_new_museum()
### Art Class Functions
- get_all_art()
### Exhibition Class Functions
- get_all_exhibition()
- get_exhibition_by_id()
- create_exhibition(status = false)
### Request Class Functions
- get_all_requests()
- create_request(start_date, end_date)


## Owner User Functionality:

### Owner Class Functions
- get_all_owner()
- create_new_owner()

### Exhibition Class Functions
- get_exhibitions()

### Request Class Functions
- show_requests()
- approve_request()
    check all other requests for exhibition. If all are approved staus == True or false, and at least 1 is true. set exhibitions status to true.  
- deny_request()

### Art Class Functions
- add_new_art()
- delete_art()  
