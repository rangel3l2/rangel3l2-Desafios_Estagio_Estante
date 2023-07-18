import { Component, OnInit } from '@angular/core';
import { School } from 'src/app/core/models/school';
import { ModalInicializatorComponent } from '../modal-inicializator/modal-inicializator.component';
import {MatDialog, MAT_DIALOG_DATA, MatDialogRef, MatDialogModule} from '@angular/material/dialog';
@Component({
  selector: 'app-inicializator',
  templateUrl: './inicializator.component.html',
  styleUrls: ['./inicializator.component.scss']
})
export class InicializatorComponent implements OnInit {
  name?: string;
  address?: string;
  phone?: string;
  type?: string;
  quantity?: number;
  school?: School
  ngOnInit(): void {

  }
  constructor(public dialog: MatDialog) {}

    openDialog(): void {
      const dialogRef = this.dialog.open(ModalInicializatorComponent, {
        width: '250px',

        data: {name: this.quantity, type: this.type, },
      });

      
      dialogRef.afterClosed().subscribe(result => {
        this.school= result

       })
  }


}

