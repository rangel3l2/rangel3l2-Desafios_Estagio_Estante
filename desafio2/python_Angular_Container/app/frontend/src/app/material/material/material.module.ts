import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {MatIconModule} from '@angular/material/icon';
import {MatDialogModule} from '@angular/material/dialog';
import {MatButtonModule} from '@angular/material/button';
import {MatInputModule} from '@angular/material/input';
import {MatFormFieldModule} from '@angular/material/form-field'
import {MatRadioModule} from '@angular/material/radio';

const COMPONENTS = [
  MatIconModule, 
  MatDialogModule,
  MatButtonModule,
  MatInputModule,
  MatFormFieldModule, 
  MatRadioModule,

]

@NgModule({
  declarations: [],
  imports: [
    CommonModule
  ],
  exports: [
    COMPONENTS,
  ]
})
export class MaterialModule { }
